import re

"""Parser for files of StereoGene pipeline and objects for parser"""

class Run:
	"""
	All about the run class
	"""
	def __init__(self, path, track1_id, track2_id, param_id, prog_run_id, nFgr, Bkg_av, Fg_av, Bkg_sd, Fg_sd, tot_cor, mann_z, p_value,
pc):
		"""
		Basic constructor
		"""
		self.table_id = None
		self.track1_id = track1_id
		self.track2_id = track2_id
		self.param_id = param_id
		self.prog_run_id = prog_run_id
		self.nFgr = nFgr
		self.Bkg_av = Bkg_av
		self.Fg_av = Fg_av
		self.Bkg_sd = Bkg_sd
		self.Fg_sd = Fg_sd
		self.tot_cor = tot_cor
		self.mann_z = mann_z
		self.p_value = p_value
		self.pc = pc
		
		self.run_file_name = self.getRunFile(track1_id, track2_id, path)

		
	def getRunFile(self, track1, track2, path):
		"""
		Form result file name from input file names
		"""
		ss1 = track1.split(".")
		tissue1 = ss1[1]
		feature1 = ss1[2]
		
		ss2 = track2.split(".")
		tissue2 = ss2[1]
		feature2 = ss2[2]
		
		
		if tissue1 == tissue2:
			path += "/tissues/" + tissue1 + "/"
		else:
			path += "/features/" + feature1 + "/"
		
		point1 = track1.rfind(".")
		point2 = track2.rfind(".")
		return path + track1[0:point1] + "~" + track2[0:point2]

	def __str__(self):
		"""
		Form string representation 
		"""
		return "%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s" % (self.table_id, self.track1_id, self.track2_id, self.param_id, self.prog_run_id, self.nFgr, self.Bkg_av, self.Fg_av, self.Bkg_sd, self.Fg_sd, self.tot_cor, self.mann_z, self.p_value, self.pc)




class Track:#
	"""
	All about the track class
	"""
	def __init__(self, mark_id, sample_id, lab_id, tissue_id=None, devstage_id=None):
		"""
		Basic constructor
		"""
		self.table_id = None
		self.tissue_id = tissue_id
		self.mark_id = mark_id
		self.sample_id = sample_id
		self.lab_id = lab_id
		self.devstage_id = devstage_id		

	def set_id(self, table_id):
		"""
		Set id for object
		"""
		self.table_id = table_id

class Param:
	"""
	Class to store the parameters of running
	"""
	def __init__(self, paramHash):
		self.paramHash = paramHash

class Parser:
	"""
	Parser of results
	"""
	def parseHEAtrack(self, track_name):#
		"""
		Parse track name in Human Epigenom Atlas format(for example UCSF_UBC.Fetal_Brain.H3K27me3.HuFNSC01.wig)
		Return object of class Track
		"""
		ss = track_name.split(".")
		lab_id = ss[0]
		tissue_id = ss[1]
		mark_id = ss[2]
		sample_id = ".".join(ss[3:(len(ss)-1)])
		
		return Track(mark_id, sample_id, lab_id, tissue_id)
	
	def parseStatistic(self, fname, param_id, resultPath):
		"""
		Parse statistic file
		param_id, resultPath are needed to form Run objects
		Return:
			tracks - dict of Track objects
			runList - list of Run objects
			labs - set of laboratory names
			tissues - set of tissues
			marks - set of marcs
			samples - set of samples
		"""
		runList = []
		fin = open(fname)
		tracks = {}
		labs = set()
		tissues = set()
		marks = set()
		samples = set()
	
		for line in fin:
			if line.startswith("id"):
				ids = line.split()
				continue
			ss = line.split()
			data = {}
			for i in range(len(ids)):
				data[ids[i]]=ss[i]
			
			prog_run_id = data["id"]
			#read track1, put to the list
			track1_id = data["name1"]
			if track1_id not in tracks:
				track1 = self.parseHEAtrack(track1_id)#specific for Human Epigenome Atlas
				labs.add(track1.lab_id)
				tissues.add(track1.tissue_id)
				marks.add(track1.mark_id)
				samples.add(track1.sample_id)
				tracks[track1_id] = track1
			
			#read track2, put to the list
			track2_id = data["name2"]
			if track2_id not in tracks:
				track2 = self.parseHEAtrack(track2_id)#specific for Human Epigenome Atlas
				labs.add(track2.lab_id)
				tissues.add(track2.tissue_id)
				marks.add(track2.mark_id)
				samples.add(track2.sample_id)
				tracks[track2_id] = track2
			#read other params
			
		
			runList.append(Run(resultPath, track1_id, track2_id, param_id, prog_run_id, data["nFgr"], data["Bkg_av"], data["Fg_av"], data["Bkg_sd"], data["Fg_sd"], data["tot_cor"], data["Mann-Z"], data["p-value"],
	data["pc"]))
		fin.close()

		return	tracks, runList, labs, tissues, marks, samples 
	
	def parseChrom(self, fname):
		"""
		Parse file with chromosome sizes
		Return hash of chromosome sizes
		"""
		fin = open(fname)
		chrom_hash = {}

		for line in fin:
			if line.startswith("#"):
				continue
			ss = line.split()
			chrom = ss[0]	
			size = ss[1]

			chrom_hash[chrom] = size	

		fin.close()
		return(chrom_hash)
	
	def parse_dist(self, fname):
		"""
		Parse distance correlation file
		Return:
		poses - position list, 
		chrom_dist_hash - distances by chromosom hash, 
		bg_dist - background distance value list
		"""
		print(fname)
		fin = open(fname)
		i = 0
		chrom_dist_hash = {}
		bg_dist = []
		poses = []
		
		names = []
		for line in fin:
			ss = line.split()
			if (i==0):
				names.append("All")
				names.extend(ss[5:])
				for name in names:
					chrom_dist_hash[name] = []		
			else:
				poses.append(int(ss[0]))
				bg_dist.append(ss[1])
				chrom_dist_hash["All"].append(float(ss[2]))

				for i in range(5,len(names)):
					if ss[i]!="NA":
						chrom_dist_hash[names[i]].append(float(ss[i]))

			i+=1
	
		fin.close()

		return poses, chrom_dist_hash, bg_dist

	def parseBg(self, fname):
		"""
		Parse background file
		Return list of background values
		"""
		fin = open(fname)
		bg = []
		for line in fin:
			bg.append(line.strip())


		fin.close()
		return(bg)

	def parseChromStat(self, fname):
		"""
		Parse statistic for chromosoms file
		Return dict of chromosom statistic
		"""
		fin = open(fname)
		chrom_stat = {}
		i=0
		for line in fin:
			if i < 3:
				i += 1
				continue
			chrom, av1, av2, cc, count = line.split()
			chrom_stat[chrom] = {'av1':av1, 'av2':av2, 'cc':cc, 'count':count}
		
		fin.close()
		return(chrom_stat)

	def parseFg(self, fname):
		"""
		Parse foreground file
		Return list of (chrom, start, end, score) dicts
		"""
		fin = open(fname)
		fg = []	

		for line in fin:
			chrom, start, end, score = line.split()
			fg.append({'chrom':chrom, 'start':start, 'end':end, 'score':score})

		fin.close()
		return(fg)


	def parseParam(self, fname):
		"""
		Parse parameters file
		Return dict of parameters
		"""
		fin = open(fname)
		paramHash = {}
		for line in fin:
			line = line.strip()
			if line.startswith("#"):
				continue
			ss = re.split("[ =\t;]+", line)
			print(ss)
			if ss[0].strip()=="profPath":
				paramHash["prof_path"] = ss[1].strip()
				continue
			if ss[0].strip()=="trackPath":
				paramHash["track_path"] = ss[1].strip()
				continue
			if ss[0].strip()=="resPath":
				paramHash["res_path"] = ss[1].strip()
				continue
			if ss[0].strip()=="map":
				paramHash["map"] = ss[1].strip()
				continue
			if ss[0].strip()=="pcorProfile":
				paramHash["pcor_profile"] = ss[1].strip()
				continue
			if ss[0].strip()=="wSize":
				paramHash["wSize"] = ss[1].strip()
				continue
			if ss[0].strip()=="wStep":
				paramHash["wSize"] = ss[1].strip()
				continue

		
			if ss[0].strip()=="kernelType":
				id1 = 0L
				if ss[1].strip()=="NORMAL":
					id1 = 1L
				elif ss[1].strip()=="LEFT_EXP":
					id1 = 2L
				else:
					id1 = 3L
				paramHash["kernel_type_id"] = id1


				continue

			if ss[0].strip()=="KernelSigma":
				paramHash["kernel_sigma"] = ss[1].strip()
				continue

			if ss[0].strip()=="kernelShift":
				paramHash["kernel_shift"] = ss[1].strip()
				continue
		
			if ss[0].strip()=="kernelNS":
				paramHash["kernel_NS"] = ss[1].strip()
				continue

			if ss[0].strip()=="complFg":
				ss[1] = ss[1].strip()
				id1 = 0
				if ss[1] == "COLINEAR":
					id1 = 1
				elif ss[1] == "COMPLEMENT":
					id1 = 2
				else:
					id1 = 3

				paramHash["compl_Fg_id"] = id1
				continue

			if ss[0].strip()=="statistics":
				paramHash["statistics"] = ss[1].strip()
				continue

			if ss[0].strip()=="aliases":
				paramHash["aliases"] = ss[1].strip()
				continue

			if ss[0].strip()=="log":
				paramHash["log"] = ss[1].strip()
				continue

			if ss[0].strip()=="chrom":
				paramHash["chrom"] = ss[1].strip()
				continue

			if ss[0].strip()=="na":
				paramHash["na"] = ss[1].strip()
				continue

			if ss[0].strip()=="type":

				type1 = ss[1].strip()
				id1 = 0

				if type1 == "BED":
					id1 = 1
				elif type1 == "BEDGRAPH":
					id1 = 2
				elif type1 == "WIG":
					id1 = 3
				else:
					id1 = 4
				paramHash["input_type_id"] = id1
				continue

			if ss[0].strip()=="intervals":


				intervals = ss[1].strip()
				id1 = 0

				if intervals == "NONE":
					id1 = 1
				elif intervals == "GENE":
					id1 = 2
				elif intervals == "EXON":
					id1 = 3
				elif intervals == "IVS":
					id1 = 4
				elif intervals == "GENE_BEG":
					id1 = 5
				elif intervals == "EXON_BEG":
					id1 = 6
				elif intervals == "IVS_BEG":
					id1 = 7
				elif intervals == "GENE_END":
					id1 = 8
				elif intervals == "EXON_END":
					id1 = 9
				elif intervals == "IVS_END":
					id1 = 10
				paramHash["gene_intervals_id"] = id1
				continue


			if ss[0].strip()=="strand":
				paramHash["strand"] = ss[1].strip()
				continue
		
			if ss[0].strip()=="scaleFactor":
				paramHash["scale_factor"] = ss[1].strip()
				continue

			if ss[0].strip()=="step":
				paramHash["step"] = ss[1].strip()
				continue

			if ss[0].strip()=="scale":
				scale = ss[1].strip()
				id1 = 0
				if intervals == "LOG":
					id1 = 1
				elif intervals == "LIN":
					id1 = 2
				elif intervals == "AUTO":
					id1 = 3

				paramHash["scale_id"] = id1
				continue

			if ss[0].strip()=="lAauto":
				paramHash["lAauto"] = ss[1].strip()
				continue


			if ss[0].strip()=="bpType":
				bpType = ss[1].strip()
				id1 = 0
				if bpType == "SCORE":
					id1 = 1
				elif bpType == "SIGNAL":
					id1 = 2
				elif bpType == "LOGPVAL":
					id1 = 3


				paramHash["bpType_id"] = id1
				continue
		
			if ss[0].strip()=="flankSize":
				paramHash["flankSize"] = ss[1].strip()
				continue

			if ss[0].strip()=="noiseLevel":
				paramHash["noiseLevel"] = ss[1].strip()
				continue
		
			if ss[0].strip()=="maxNA":
				paramHash["maxNA"] = ss[1].strip()
				continue

			if ss[0].strip()=="maxZero":
				paramHash["maxZero"] = ss[1].strip()
				continue
			if ss[0].strip()=="nShuffle":
				paramHash["nShuffle"] = ss[1].strip()
				continue
			if ss[0].strip()=="maxShuffle":
				paramHash["maxShuffle"] = ss[1].strip()
				continue
			if ss[0].strip()=="mapIv":
				paramHash[mapIv] = ss[1].strip()
				continue
		
			if ss[0].strip()=="threshold":
				paramHash["threshold"] = ss[1].strip()
				continue
			if ss[0].strip()=="corrOnly":
				paramHash["corrOnly"] = ss[1].strip()
				continue

			if ss[0].strip()=="outDistr":
			

				paramHash[outDistr] = ss[1].strip()
				continue


			if ss[0].strip()=="mapIv":
				dist = ss[1].strip()
				id1 =  0
				if dist == "NONE":
					id1 = 1
				elif dist == "TOTAL":
					id1 = 2
				elif dist == "DETAIL":
					id1 = 3


				paramHash["distances_output_id"] = id1
				continue

			if ss[0].strip()=="outThreshold":
				paramHash["outThreshold"] = ss[1].strip()
				continue

			if ss[0].strip()=="outSpectr":
				paramHash["outSpectr"] = ss[1].strip()
				continue
			if ss[0].strip()=="outChrom":
				paramHash["outChrom"] = ss[1].strip()
				continue
			else:
				print("some param is not found: " + ss[0])

		fin.close()

		return Param(paramHash)


	


