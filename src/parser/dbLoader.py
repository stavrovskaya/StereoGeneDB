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
		self.cnx = MySQLdb.connect(host=self.host, port = self.port, user=self.user, passwd=self.pwd, db=self.db)
		
	def disconnect(self):
		"""
		Connect
		"""
		if self.cnx:    
			self.cnx.close()
				
	
	def loadLabs(self, labs):
		"""
		Load laboratories into lab table
		"""
		ids = {}

		cursor = self.cnx.cursor()
		add_lab = ("INSERT INTO lab "
			       "(lab) "
			       "VALUES (%s)"
			       "ON DUPLICATE KEY UPDATE id= LAST_INSERT_ID(id)")
		for lab in labs:
			cursor.execute(add_lab, lab)
			lab_id = cursor.lastrowid
			ids[lab] = lab_id

		self.cnx.commit()
		cursor.close()

		return ids
			
	def loadTissues(self, tissues):
		"""
		Load tissues into corr_tissue table
		"""
		ids = {}


		cursor = self.cnx.cursor()
		add_tissue = ("INSERT INTO tissue "
			       "(tissue) "
			       "VALUES (%s)"
			       "ON DUPLICATE KEY UPDATE id= LAST_INSERT_ID(id)")
		for tissue in tissues:
			cursor.execute(add_tissue, tissue)
			tissue_id = cursor.lastrowid
			ids[tissue] = tissue_id


		self.cnx.commit()
		cursor.close()
		return ids

	def loadMarks(self, marks):
		"""
		Load marks (for example H3K4me3) into mark table
		"""
		ids = {}
		cursor = self.cnx.cursor()

		add_mark = ("INSERT INTO mark "
			       "(mark) "
			       "VALUES (%s)"
			       "ON DUPLICATE KEY UPDATE id= LAST_INSERT_ID(id)")
		for mark in marks:
			cursor.execute(add_mark, mark)
			mark_id = cursor.lastrowid
			ids[mark] = mark_id

		self.cnx.commit()
		cursor.close()

		return ids

	def loadSamples(self, samples):
		"""
		Load sample (replica id) into sample table
		"""
		ids = {}

		cursor = self.cnx.cursor()

		add_sample = ("INSERT INTO sample "
			       "(sample) "
			       "VALUES (%s)"
			       "ON DUPLICATE KEY UPDATE id= LAST_INSERT_ID(id)")
		for sample in samples:
			cursor.execute(add_sample, sample)
			sample_id = cursor.lastrowid
			ids[sample] = sample_id

		self.cnx.commit()
		cursor.close()

		return ids
	def loadDevstages(self, devstages):
		"""
		Load devstage into devstage table
		"""
		ids = {}

		cursor = self.cnx.cursor()

		add_sample = ("INSERT INTO devstage "
			       "(devstage) "
			       "VALUES (%s)"
			       "ON DUPLICATE KEY UPDATE id= LAST_INSERT_ID(id)")
		for devstage in devstages:
			cursor.execute(add_devstage, devstage)
			devstage_id = cursor.lastrowid
			ids[devstage] = devstage_id

		self.cnx.commit()
		cursor.close()

		return ids
	def loadTracks(self, tracks, mark_ids, sample_ids, lab_ids, tissue_ids=None, devstage_ids=None):
		"""
		Load tracks into track table
		"""
		ids = {}

		
		cursor = self.cnx.cursor()

		add_track_tiss = ("INSERT INTO track "
			       "(tissue_id, mark_id, sample_id, lab_id)"
			       "VALUES (%s, %s, %s, %s)"
			       "ON DUPLICATE KEY UPDATE id= LAST_INSERT_ID(id)")
		add_track_devstage = ("INSERT INTO track "
			       "(mark_id, sample_id, lab_id, devstage_id)"
			       "VALUES (%s, %s, %s, %s)"
			       "ON DUPLICATE KEY UPDATE id= LAST_INSERT_ID(id)")

		for track_name in tracks:
			track_id=None
			
			track = tracks[track_name]
			mark_id = mark_ids[track.mark_id]
			sample_id = sample_ids[track.sample_id]
			lab_id = lab_ids[track.lab_id]
			
			

			tissue_id = "NULL"
			if (track.tissue_id != None):
				tissue_id = tissue_ids[track.tissue_id]
				track_tuple = (tissue_id, mark_id, sample_id, lab_id)
				cursor.execute(add_track_tiss, track_tuple)
				track_id = cursor.lastrowid

			devstage_id = "NULL"
			if (track.devstage_id != None):
				devstage_id = devstage_ids[track.dev_stage_id]
				track_tuple = (mark_id, sample_id, lab_id, devstage_id)
				cursor.execute(add_track_devstage, track_tuple)
				track_id = cursor.lastrowid
			

			track.track_id = track_id

			ids[track_name] = track_id

		self.cnx.commit()
		cursor.close()

		return ids
	def loadOrg(self, org, version):
		"""
		Load organism (for example Homo sapiens, version hg19) into org table
		"""
		org_id = 0

		cursor = self.cnx.cursor()

		add_org = ("INSERT INTO org "
			       "(org, version) "
			       "VALUES (%s, %s)"
			       "ON DUPLICATE KEY UPDATE id= LAST_INSERT_ID(id)")
		cursor.execute(add_org, (org, version))
		org_id = cursor.lastrowid
		
		self.cnx.commit()
		cursor.close()
		

		return org_id

	def loadChroms(self, org_id, chroms):
		"""
		Load chomosoms into chrom table
		"""
		ids = {}

		cursor = self.cnx.cursor()

		add_chrom = ("INSERT INTO chrom "
			       "(org_id, chrom, size) "
			       "VALUES (%s, %s, %s)"
			       "ON DUPLICATE KEY UPDATE id= LAST_INSERT_ID(id)")

		
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
	
		return ids
		
	def loadBg(self, run_id, bg_corr, bg_dist):
		"""
		Load background into bkg table
		"""
		bg_id = 0

		cursor = self.cnx.cursor()

		add_bg = ("INSERT INTO bkg "
			       "(run_id, bkg_corr, bkg_dist_corr) "
			       "VALUES (%s, %s, %s)"
			       "ON DUPLICATE KEY UPDATE id= LAST_INSERT_ID(id)")		
		cursor.execute(add_bg, (run_id, "\t".join(bg_corr), "\t".join(bg_dist)))
		bg_id = cursor.lastrowid
		
		self.cnx.commit()
		cursor.close()
		
		return bg_id

	def loadChromStat(self, run_id, chrom_stat, chroms):
		"""
		Load total correlation statistic by chromosoms into chrom_stat table
		"""
		chrom_stat_ids = []

		cursor = self.cnx.cursor()

		add_chrom_stat = ("INSERT INTO chrom_stat "
			       "(run_id, chrom_id, track1_av, track2_av, cc, count) "
			       "VALUES (%s, %s, %s, %s, %s, %s)"
			       "ON DUPLICATE KEY UPDATE id= LAST_INSERT_ID(id)")

		for chrom in chrom_stat:
			chrom_id = chroms[chrom]
			cursor.execute(add_chrom_stat, (run_id, chrom_id, chrom_stat[chrom]['av1'], chrom_stat[chrom]['av2'], chrom_stat[chrom]['cc'], chrom_stat[chrom]['count']))
			chrom_stat_ids.append(cursor.lastrowid)
		
		self.cnx.commit()
		cursor.close()
		
		return chrom_stat_ids

	def loadFg(self, run_id, fg_corr, chroms):
		"""
		Load foreground by windows into corr_corr_fg table
		"""
		fg_ids = []

		cursor = self.cnx.cursor()

		add_fg = ("INSERT INTO corr_fg "
			       "(run_id, chrom_id, start, end, corr) "
			       "VALUES (%s, %s, %s, %s, %s)"
			       "ON DUPLICATE KEY UPDATE id= LAST_INSERT_ID(id)")		
		for fg in fg_corr:
			chrom = fg['chrom']
			cursor.execute(add_fg, (run_id, chroms[chrom], fg['start'], fg['end'], fg['score']))
			fg_id = cursor.lastrowid
			fg_ids.append(fg_id)
		
		self.cnx.commit()
		cursor.close()
		
		return fg_ids		

	def loadParams(self, param):
		"""
		Load run parameters by windows into param table
		"""

		cursor = self.cnx.cursor()

		
		var_list = param.paramHash.keys()

		values = []
		var_names = ",".join(var_list)
		print("count comma: %d" % var_names.count(","))
		var_values = ""
		ss = []
		for key in var_list:

			values.append(str(param.paramHash[key]))	
			ss.append("%s")


		var_values = ",".join(ss)

				
		add_param = ("INSERT INTO param "
			       "(" + var_names + ") "
			       "VALUES (" + var_values + ")")
		print(add_param)
		
		cursor.execute(add_param, values)
		param_id = cursor.lastrowid
 		
		self.cnx.commit()
		cursor.close()
		
		return param_id

	def loadRun(self, run, track_ids, param_id):
		"""
		Load all about the run into corr_run table
		"""
		
		cursor = self.cnx.cursor()

		add_run = ("INSERT INTO run "
			 	"(track1_id, track2_id, param_id, prog_run_id, nFgr, Bkg_av, Fg_av, Bkg_sd, Fg_sd, tot_cor, mann_z, p_value, pc)"
				" VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
		track1_id = track_ids[run.track1_id]
		track2_id = track_ids[run.track2_id]

		cursor.execute(add_run, (track1_id, track2_id, param_id, run.prog_run_id, run.nFgr, run.Bkg_av, run.Fg_av, run.Bkg_sd, run.Fg_sd, run.tot_cor, run.mann_z, run.p_value, run.pc))
		run_id = cursor.lastrowid
 		
				
	
		self.cnx.commit()
		cursor.close()
		

		return run_id

	def loadDist(self, chrom_dist_hash, run_id, chrom_ids, poses):
		"""
		Load distance correlation into dist_corr table
		"""
		dist_ids = []

		cursor = self.cnx.cursor()




		add_dist = ("INSERT INTO dist_corr "
			       "(chrom_id, dist, corr, run_id) "
			       "VALUES (%s, %s, %s, %s)"
			       "ON DUPLICATE KEY UPDATE id= LAST_INSERT_ID(id)")		
		for chrom in chrom_dist_hash:
			chrom_id = chrom_ids[chrom]
			corr = chrom_dist_hash[chrom]
			for i in range(len(corr)):
				cursor.execute(add_dist, (chrom_id, poses[i], corr[i], run_id))
			dist_id = cursor.lastrowid
			dist_ids.append(dist_id)
		
		self.cnx.commit()
		cursor.close()

		return dist_ids		
	

