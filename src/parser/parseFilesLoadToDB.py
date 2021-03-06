from dbLoader import DBloader
from stereoGeneParser import Parser
import sys



#====Parse function============
def parseStereoGeneResultFromStatistics(organism, assembly, chromLengthFile, statFile, filesInfoFile, paramFile, host, user, pwd, db, port):
	"""
	Load result into database
	"""
	parser = Parser()
	dbloader = DBloader(host=host, port = port, user=user, pwd=pwd, db = db)
	dbloader.connect()
	
	labs = []
	tissues = []
	marks = []
	samples = []


#Parse pipeline:
#load organism
	org_id = dbloader.loadOrg(organism, assembly)
	
#read chromosom length file
#load chrom lengths to db
	chroms = parser.parseChrom(chromLengthFile)	
	chrom_ids = dbloader.loadChroms(org_id, chroms)

#read files info file
	fileInfoHash = parser.parseInputFileInfoTable(filesInfoFile)

#load params
#read params file
#load params to db
	runParam, runTrackPaths, runResultPaths, confounderNames = parser.parseParam(paramFile)
	paramIdHash = {}
	for runId in runParam:
		paramIdHash[runId] = dbloader.loadParams(runParam[runId])
		
	
#read statistics file
	tracks, runList, trackPaths, labs, tissues, devstages, marks, samples, confounders = parser.parseStatistic(statFile, runTrackPaths, runResultPaths, fileInfoHash, confounderNames)

#load confounders, if exist
	confounderIdHash = None
	confounderPath = paramFile[0:paramFile.rfind("/") + 1]
	if len(confounders)!=0:
		confounderIdHash = {}
		for confounder in confounders:
			confounderName, confounderMemberPath = confounder
			confounderMembers, memberPaths = parser.parseConfounder(confounderPath + confounderName + ".cvr", confounderMemberPath)
			memberPathIds = dbloader.loadTrackPaths(memberPaths)
			
			confounderId = dbloader.loadConfounder(confounderName)
			
			dbloader.loadConfounderMembers(confounderId, confounderMembers, memberPathIds)
			
			confounderIdHash[confounderName] = confounderId 

#load trackPaths
	track_path_ids = dbloader.loadTrackPaths(trackPaths)

#load labs
	lab_ids = dbloader.loadLabs(labs)
#load tissues
	tissue_ids = dbloader.loadTissues(tissues)
#load devstages
	devstage_ids = dbloader.loadDevstages(devstages)
	print(devstage_ids)
#load marks
	mark_ids = dbloader.loadMarks(marks)	
#load samples
	sample_ids = dbloader.loadSamples(samples)
	print(sample_ids)
#load tracks
	track_ids = dbloader.loadTracks(tracks, track_path_ids, mark_ids, sample_ids, lab_ids, tissue_ids, devstage_ids)
#	for each run
	for run in runList:	
#		load param
		param_id = paramIdHash[run.prog_run_id]
#		load run statistic
		run_id = dbloader.loadRun(run, track_ids, param_id, confounderIdHash)

#		get run name to make chrom file name
		chrom_file = run.run_file_name + ".chrom"

#		read chrom statistic

#		chrom_stat = parser.parseChromStat(chrom_file)

#		load chrom statistic
#		chrom_stat_id = dbloader.loadChromStat(run_id, chrom_stat, chrom_ids)

#		load dist
		dist_file = run.run_file_name + ".dist"		
		chrom_dist_hash, bg_dist = parser.parse_dist(dist_file)
		

		
		dbloader.loadDist(chrom_dist_hash, run_id, chrom_ids)

#		load bg
		bg_fname = run.run_file_name + ".bkg"	
		bg_corr = parser.parseBg(bg_fname)
		bg_id = dbloader.loadBg(run_id, bg_corr, bg_dist)
#		load fg
		fg_fname = run.run_file_name + ".fg"	
		fg = parser.parseFg(fg_fname)
		fg_id = dbloader.loadFg(run_id, fg, chrom_ids)

	dbloader.disconnect()

#====================main programm====================


# read params from command line

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-o", "--organism", type=str,
                    help="Organism id")
parser.add_argument("-a", "--assembly",  type=str,
                    help="Genome assebly")
parser.add_argument("-chr", "--chromLengthFile", type=str,
                    help="Path to the file with chromosom lengths")
parser.add_argument("-st", "--statFile",  type=str,
                    help="Path to the of statistics file")
parser.add_argument("-prm", "--paramFile", type=str,
                    help="Path to the params file")
parser.add_argument("-fi", "--fileInfo",  type=str,
                    help="Path to track information file")
parser.add_argument("-ho", "--host",  type=str,
                    help="Database host")
parser.add_argument("-d", "--db",  type=str,
                    help="Database")
parser.add_argument("-u", "--user",  type=str,
                    help="db user")
parser.add_argument("-p", "--pwd",  type=str,
                    help="Database password")
parser.add_argument("-po", "--port",  type=int,
                    help="Database port")

args = parser.parse_args()

print(args)


parseStereoGeneResultFromStatistics(args.organism, args.assembly, args.chromLengthFile, args.statFile, args.fileInfo,  args.paramFile, args.host, args.user, args.pwd, args.db, args.port)


