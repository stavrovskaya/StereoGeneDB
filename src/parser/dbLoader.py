import MySQLdb
from stereoGeneParser import Param
from stereoGeneParser import Run
from stereoGeneParser import Track

"""
Load StereoGene results to database modul
"""
class DBloader:
	"""
	Class for data loading
	"""
	def __init__(self, host, port, db, user, pwd):
		"""
		Basic constructor
		"""
		self.host = host
		self.port = port
		self.db = db
		self.user = user
		self.pwd = pwd
	def connect(self):
		"""
		Connect
		"""
		print("in connect: host=%s, port=%s, user=%s, password=%s, db=%s"%(self.host, self.port, self.user, self.pwd, self.db))
		self.cnx = MySQLdb.connect(host=self.host, port = self.port, user=self.user, passwd=self.pwd, db=self.db)
		
	def disconnect(self):
		"""
		Connect
		"""
		if self.cnx:    
			self.cnx.close()
				
	def loadTrackPath(self, path):
		"""
		Load path (input track) into db
		"""
		print(path)
		cursor = self.cnx.cursor()
		add_track_path = ("""INSERT INTO track_path 
			       (track_path) 
			       VALUES (%s)
			       ON DUPLICATE KEY UPDATE id= LAST_INSERT_ID(id)""")
		
		cursor.execute(add_track_path, [path])
		track_path_id = cursor.lastrowid
		
		self.cnx.commit()
		cursor.close()

		return(track_path_id)
		
	def loadTrackPaths(self, trackPaths):
		"""
		Load set of paths (input track) into db
		"""
		ids = {}
		
		cursor = self.cnx.cursor()
		add_track_path = ("""INSERT INTO track_path 
			       (track_path) 
			       VALUES (%s)
			       ON DUPLICATE KEY UPDATE id= LAST_INSERT_ID(id)""")
		
		for path in trackPaths:
			print(path)
			cursor.execute(add_track_path, [path])
			track_path_id = cursor.lastrowid
			ids[path] = track_path_id
		
		self.cnx.commit()
		cursor.close()
		
		return(ids)
		
	def loadLabs(self, labs):
		"""
		Load laboratories into lab table
		"""
		ids = {}

		cursor = self.cnx.cursor()
		add_lab = ("""INSERT INTO lab 
			       (lab) 
			       VALUES (%s)
			       ON DUPLICATE KEY UPDATE id= LAST_INSERT_ID(id)""")
		for lab in labs:
			cursor.execute(add_lab, [lab])
			lab_id = cursor.lastrowid
			ids[lab] = lab_id

		self.cnx.commit()
		cursor.close()

		return(ids)
			
	def loadTissues(self, tissues):
		"""
		Load tissues into tissue table
		"""
		ids = {}


		cursor = self.cnx.cursor()
		add_tissue = ("""INSERT INTO tissue 
			       (tissue) 
			       VALUES (%s)
			       ON DUPLICATE KEY UPDATE id= LAST_INSERT_ID(id)""")
		for tissue in tissues:
			cursor.execute(add_tissue, [tissue])
			tissue_id = cursor.lastrowid
			ids[tissue] = tissue_id


		self.cnx.commit()
		cursor.close()
		return(ids)
	def loadDevstages(self, devstages):
		"""
		Load tissues into devstage table
		"""
		ids = {}


		cursor = self.cnx.cursor()
		add_devstage = ("""INSERT INTO devstage 
			       (devstage) 
			       VALUES (%s)
			       ON DUPLICATE KEY UPDATE id= LAST_INSERT_ID(id)""")
		for devstage in devstages:
			cursor.execute(add_devstage, [devstage])
			devstage_id = cursor.lastrowid
			ids[devstage] = devstage_id


		self.cnx.commit()
		cursor.close()
		return(ids)
	def loadMarks(self, marks):
		"""
		Load marks (for example H3K4me3) into mark table
		"""
		ids = {}
		cursor = self.cnx.cursor()

		add_mark = ("""INSERT INTO mark 
			       (mark) 
			       VALUES (%s)
			       ON DUPLICATE KEY UPDATE id= LAST_INSERT_ID(id)""")
		for mark in marks:
			cursor.execute(add_mark, [mark])
			mark_id = cursor.lastrowid
			ids[mark] = mark_id

		self.cnx.commit()
		cursor.close()

		return(ids)

	def loadSamples(self, samples):
		print(samples)
		"""
		Load sample (replica id) into sample table
		"""
		ids = {}

		cursor = self.cnx.cursor()

		add_sample = ("""INSERT INTO sample 
			       (sample) 
			       VALUES (%s)
			       ON DUPLICATE KEY UPDATE id= LAST_INSERT_ID(id)""")
		for sample in samples:
			cursor.execute(add_sample, [sample])
			sample_id = cursor.lastrowid
			ids[sample] = sample_id

		self.cnx.commit()
		cursor.close()

		return(ids)
	def loadDevstages(self, devstages):
		"""
		Load devstage into devstage table
		"""
		ids = {}

		cursor = self.cnx.cursor()

		add_devstage = ("""INSERT INTO devstage 
			       (devstage) 
			       VALUES (%s)
			       ON DUPLICATE KEY UPDATE id= LAST_INSERT_ID(id)""") #was add_sample
		for devstage in devstages:
			cursor.execute(add_devstage, [devstage])
			devstage_id = cursor.lastrowid
			ids[devstage] = devstage_id

		self.cnx.commit()
		cursor.close()

		return(ids)
	def loadTracks(self, tracks, track_path_ids, mark_ids, sample_ids, lab_ids, tissue_ids=None, devstage_ids=None):
		"""
		Load tracks into track table
		"""
		ids = {}

		
		cursor = self.cnx.cursor()

		add_track_tiss = ("""INSERT INTO track 
			       (track_name, tissue_id, mark_id, sample_id, lab_id, track_path_id)
			       VALUES (%s, %s, %s, %s, %s, %s)
			       ON DUPLICATE KEY UPDATE id= LAST_INSERT_ID(id)""")
		add_track_devstage = ("""INSERT INTO track 
			       (track_name, mark_id, sample_id, lab_id, devstage_id, track_path_id)
			       VALUES (%s, %s, %s, %s, %s, %s)
			       ON DUPLICATE KEY UPDATE id= LAST_INSERT_ID(id)""")
		add_track_tiss_no_sample = ("""INSERT INTO track 
			       (track_name, tissue_id, mark_id, lab_id, track_path_id)
			       VALUES (%s, %s, %s, %s, %s)
			       ON DUPLICATE KEY UPDATE id= LAST_INSERT_ID(id)""")
		add_track_devstage_no_sample = ("""INSERT INTO track 
			       (track_name, mark_id, lab_id, devstage_id, track_path_id)
			       VALUES (%s, %s, %s, %s, %s)
			       ON DUPLICATE KEY UPDATE id= LAST_INSERT_ID(id)""")

		for track_name_path in tracks:
			track_id=None
			
			track = tracks[track_name_path]
			track_name = track_name_path[1]
			mark_id = mark_ids[track.mark]
			sample_id = sample_ids.get(track.sample, "NULL")
			lab_id = lab_ids[track.lab]
			track_path_id = track_path_ids[track.trackPath]
			
			

			tissue_id = "NULL"
			if (track.tissue != None):
				tissue_id = tissue_ids[track.tissue]
				if (sample_id != "NULL"):
					track_tuple = (track_name, tissue_id, mark_id, sample_id, lab_id, track_path_id)
					cursor.execute(add_track_tiss, track_tuple)
					track_id = cursor.lastrowid
				else:
					track_tuple = (track_name, tissue_id, mark_id, lab_id, track_path_id)
					cursor.execute(add_track_tiss_no_sample, track_tuple)
					track_id = cursor.lastrowid
				
			devstage_id = "NULL"
			if (track.devstage != None):
				devstage_id = devstage_ids[track.devstage] # was track.dev_stage
				if (sample_id != "NULL"):
					track_tuple = (track_name, mark_id, sample_id, lab_id, devstage_id, track_path_id)
					cursor.execute(add_track_devstage, track_tuple)
					track_id = cursor.lastrowid
				else:
					track_tuple = (track_name, mark_id, lab_id, devstage_id, track_path_id)
					cursor.execute(add_track_devstage_no_sample, track_tuple)
					track_id = cursor.lastrowid
			

			track.track_id = track_id

			ids[track_name_path] = track_id

		self.cnx.commit()
		cursor.close()

		return(ids)
	def loadOrg(self, org, assembly):
		"""
		Load organism (for example Homo sapiens, version hg19) into org table
		"""
		org_id = 0

		cursor = self.cnx.cursor()

		add_org = ("""INSERT INTO org 
			       (org, assembly) 
			       VALUES (%s, %s)
			       ON DUPLICATE KEY UPDATE id= LAST_INSERT_ID(id)""")
		cursor.execute(add_org, (org, [assembly]))
		org_id = cursor.lastrowid
		
		self.cnx.commit()
		cursor.close()
		

		return(org_id)

	def loadChroms(self, org_id, chroms):
		"""
		Load chomosoms into chrom table
		"""
		ids = {}

		cursor = self.cnx.cursor()

		add_chrom = ("""INSERT INTO chrom 
			       (org_id, chrom, size) 
			       VALUES (%s, %s, %s)
			       ON DUPLICATE KEY UPDATE id= LAST_INSERT_ID(id)""")

		
		for chrom in chroms:
			size = chroms[chrom]

			cursor.execute(add_chrom, (org_id, chrom, size))
			chrom_id = cursor.lastrowid
			ids[chrom] = chrom_id
			
		

		cursor.execute(add_chrom, (org_id, "All", 0))
		chrom_id = cursor.lastrowid
		ids["All"] = chrom_id


		self.cnx.commit()
		cursor.close()
	
		return(ids)
		
	def loadBg(self, run_id, bg_corr, bg_dist):
		"""
		Load background into bkg table
		"""
		bg_id = 0

		cursor = self.cnx.cursor()

		add_bg = ("""INSERT INTO bkg 
			       (run_id, bkg_corr, bkg_dist_corr) 
			       VALUES (%s, %s, %s)
			       ON DUPLICATE KEY UPDATE id= LAST_INSERT_ID(id)""")		
		cursor.execute(add_bg, (run_id, "\t".join(bg_corr), "\t".join(bg_dist)))
		bg_id = cursor.lastrowid
		
		self.cnx.commit()
		cursor.close()
		
		return(bg_id)

	def loadChromStat(self, run_id, chrom_stat, chroms):
		"""
		Load total correlation statistic by chromosoms into chrom_stat table
		"""
		chrom_stat_ids = []

		cursor = self.cnx.cursor()

		add_chrom_stat = ("""INSERT INTO chrom_stat 
			       (run_id, chrom_id, track1_av, track2_av, cc, count) 
			       VALUES (%s, %s, %s, %s, %s, %s)
			       ON DUPLICATE KEY UPDATE id= LAST_INSERT_ID(id)""")

		for chrom in chrom_stat:
			chrom_id = chroms[chrom]
			cursor.execute(add_chrom_stat, (run_id, chrom_id, chrom_stat[chrom]['av1'], chrom_stat[chrom]['av2'], chrom_stat[chrom]['cc'], chrom_stat[chrom]['count']))
			chrom_stat_ids.append(cursor.lastrowid)
		
		self.cnx.commit()
		cursor.close()
		
		return(chrom_stat_ids)

	def loadFg(self, run_id, fg_corr, chroms):
		"""
		Load foreground by windows into fg table
		"""
		fg_ids = []

		cursor = self.cnx.cursor()

		add_fg = ("""INSERT INTO fg 
			       (run_id, chrom_id, corr) 
			       VALUES (%s, %s, %s)
			       ON DUPLICATE KEY UPDATE id= LAST_INSERT_ID(id)""")		
		for chrom in fg_corr:
			cursor.execute(add_fg, (run_id, chroms[chrom], "\t".join(fg_corr[chrom])))
			fg_id = cursor.lastrowid
			fg_ids.append(fg_id)
		
		self.cnx.commit()
		cursor.close()
		
		return(fg_ids)		

	def loadParams(self, param):
		"""
		Load run parameters by windows into param table
		"""

		cursor = self.cnx.cursor()

		
		var_list = param.paramHash.keys()

		values = []
		var_names = ",".join(var_list)
		var_select_names = "=%s and ".join(var_list) + "=%s"
		
		var_values = ""
		ss = []
		for key in var_list:

			values.append(str(param.paramHash[key]))	
			ss.append("%s")


		var_values = ",".join(ss)

				
		check_param = ("SELECT id "
				"FROM param "
				"WHERE " + var_select_names
		)
		add_param = ("INSERT INTO param" 
			       "(" + var_names + ")" 
			       "VALUES (" + var_values + ")")

		
		#check if exist
		cursor.execute(check_param, values)
		param_id = cursor.fetchone()
		if (param_id != None):
			return(param_id[0])
		cursor.execute(add_param, values)
		param_id = cursor.lastrowid
 		
		self.cnx.commit()
		cursor.close()
		
		return(param_id)

	def loadRun(self, run, track_ids, param_id, confounder_ids):
		"""
		Load all about the run into corr_run table
		"""

		cursor = self.cnx.cursor()
#		nFgr, nBkg, Fg_Corr, Fg_av_Corr, FgCorr_sd, Bg_Corr, Bg_av_Corr, BgCorr_sd, mann_z, p_value, pc

		add_run = ("""INSERT INTO run 
			 	(track1_id, track2_id, param_id, prog_run_id, nFgr, nBkg, Fg_Corr, Fg_av_Corr, FgCorr_sd, Bg_Corr, Bg_av_Corr, BgCorr_sd, mann_z, p_value, date, confounder_id)
				 VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
				 ON DUPLICATE KEY UPDATE id= LAST_INSERT_ID(id)""")
		add_run_no_confounder = ("""INSERT INTO run 
			 	(track1_id, track2_id, param_id, prog_run_id, nFgr, nBkg, Fg_Corr, Fg_av_Corr, FgCorr_sd, Bg_Corr, Bg_av_Corr, BgCorr_sd, mann_z, p_value, date)
				 VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
				 ON DUPLICATE KEY UPDATE id= LAST_INSERT_ID(id)""")
		track1_id = track_ids[run.track1_id]
		track2_id = track_ids[run.track2_id]
		if run.confounder_id is None:
			cursor.execute(add_run_no_confounder, (track1_id, track2_id, param_id, run.prog_run_id, run.nFgr, run.nBkg, run.Fg_Corr, run.Fg_av_Corr, run.FgCorr_sd, run.Bg_Corr, run.Bg_av_Corr, run.BgCorr_sd, run.mann_z, run.p_value, run.date))
			run_id = cursor.lastrowid
 		else:
			confounder_id = confounder_ids[run.confounder_id]
			cursor.execute(add_run, (track1_id, track2_id, param_id, run.prog_run_id, run.nFgr, run.nBkg, run.Fg_Corr, run.Fg_av_Corr, run.FgCorr_sd, run.Bg_Corr, run.Bg_av_Corr, run.BgCorr_sd, run.mann_z, run.p_value, run.date, confounder_id))
			run_id = cursor.lastrowid
 		
				
	
		self.cnx.commit()
		cursor.close()
		

		return(run_id)

	def loadDist(self, chrom_dist_hash, run_id, chrom_ids):
		"""
		Load distance correlation into dist_corr table
		"""
		dist_ids = []

		cursor = self.cnx.cursor()
		add_dist = ("""INSERT INTO dist_corr 
			       (chrom_id, dist, corr, run_id) 
			       VALUES (%s, %s, %s, %s)
			       ON DUPLICATE KEY UPDATE id= LAST_INSERT_ID(id)""")		
		for chrom in chrom_dist_hash:
			
			chrom_id = chrom_ids[chrom]
			corr_list = chrom_dist_hash[chrom]
			for corr_data in corr_list:
				pose = corr_data[0]
				corr = corr_data[1]
				cursor.execute(add_dist, (chrom_id, pose, corr, run_id))
				dist_id = cursor.lastrowid
				dist_ids.append(dist_id)
		
		self.cnx.commit()
		cursor.close()

		return(dist_ids)
	def loadConfounder(self, confounder_name):
	
		"""
		Load confounder name into db
		"""
		print(confounder_name)
		cursor = self.cnx.cursor()
		add_confounder = ("""INSERT INTO confounder 
			       (confounder_name) 
			       VALUES (%s)
			       ON DUPLICATE KEY UPDATE id= LAST_INSERT_ID(id)""")
		
		cursor.execute(add_confounder, [confounder_name])
		confounder_id = cursor.lastrowid
		
		self.cnx.commit()
		cursor.close()

		return(confounder_id)
		
	def loadConfounderMembers(self, confounder_id, confounder_members, member_path_ids):
	
		"""
		Load confounder name into db
		"""
		member_ids = []
		print("confounder_members=" + str(confounder_members))

		cursor = self.cnx.cursor()
		add_member = ("""INSERT INTO confounder_member 
			       (confounder_id, member_name, member_path_id, eigen_value) 
			       VALUES (%s, %s, %s, %s)
			       ON DUPLICATE KEY UPDATE id= LAST_INSERT_ID(id)""")		
		for member_name in confounder_members:
			member = confounder_members[member_name]
			eigen_value = str(int(100*member.eigenValue))
			member_path_id = member_path_ids[member.path]
			cursor.execute(add_member, (confounder_id, member_name, member_path_id, eigen_value))
			member_id = cursor.lastrowid
			member_ids.append(member_id)
		
		self.cnx.commit()
		cursor.close()

		return(member_ids)
