from dbLoader import DBloader
from stereoGeneParser import Parser



#====Parse function============
def parseHEAstereoGeneFromStatistics(organism, version, chromLengthFile, statFile, paramFile, resultPath):
	"""
	Load Human Epigenome Atlas result into database
	"""
	parser = Parser()
	dbloader = DBloader(host="node13", port = 3306, user="lena", pwd="theeHuz9", db = "markup_corr_2014")
	dbloader.connect()
	
	labs = []
	tissues = []
	marks = []
	samples = []

#Parse pipeline:
#load organism
	org_id = dbloader.loadOrg(organism, version)
	
#read chromosom length file
#load chrom lengths to db
	chroms = parser.parseChrom(chromLengthFile)	
	chrom_ids = dbloader.loadChroms(org_id, chroms)
	
#read params files
#load params to db
	param = parser.parseParam(paramFile)
	param_id = dbloader.loadParams(param)
	
#read statistics file
	tracks, runList, labs, tissues, marks, samples = parser.parseStatistic(statFile, param_id, resultPath)
#load labs
	lab_ids = dbloader.loadLabs(labs)
#load tissues
	tissue_ids = dbloader.loadTissues(tissues)
#load marks
	mark_ids = dbloader.loadMarks(marks)	
#load samples
	sample_ids = dbloader.loadSamples(samples)
	print(sample_ids)
#load tracks
	track_ids = dbloader.loadTracks(tracks, mark_ids, sample_ids, lab_ids, tissue_ids)
#	for each run
	for run in runList:	
#		load run statistic
		run_id = dbloader.loadRun(run, track_ids, param_id)

#		get run name to make chrom file name
		chrom_file = run.run_file_name + ".chrom"

#		read chrom statistic

		chrom_stat = parser.parseChromStat(chrom_file)

#		load chrom statistic
		chrom_stat_id = dbloader.loadChromStat(run_id, chrom_stat, chrom_ids)

#		load dist
		dist_file = run.run_file_name + ".dist"		
		poses, chrom_dist_hash, bg_dist = parser.parse_dist(dist_file)
		
		dbloader.loadDist(chrom_dist_hash, run_id, chrom_ids, poses)

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
parser.add_argument("-v", "--version",  type=str,
                    help="Genome version")
parser.add_argument("-chr", "--chromLengthFile", type=str,
                    help="Path to the file with chromosom lengths")
parser.add_argument("-st", "--statFile",  type=str,
                    help="Path to the of statistics file")
parser.add_argument("-cf", "--configFile", type=str,
                    help="Path to the config file")
parser.add_argument("-rp", "--resultPath",  type=str,
                    help="Path to result directory")
args = parser.parse_args()

print(args)


parseHEAstereoGeneFromStatistics(args.organism, args.version, args.chromLengthFile, args.statFile, args.configFile, args.resultPath)





