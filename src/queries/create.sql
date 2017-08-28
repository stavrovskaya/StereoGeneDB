

CREATE TABLE  outWig_param (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `outWig` varchar(20) COLLATE latin1_general_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci;


CREATE TABLE  dist_output_param (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `dist_output` varchar(10) COLLATE latin1_general_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci;


CREATE TABLE  kernelType_param (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `kernel_type` varchar(10) COLLATE latin1_general_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci;



CREATE TABLE  complFg_param (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `complFg` varchar(20) COLLATE latin1_general_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci;



CREATE TABLE  bpType_param(
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `bpType` varchar(10) COLLATE latin1_general_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci;

CREATE TABLE  intervals_param(
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `intervals` varchar(10) COLLATE latin1_general_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci;

CREATE TABLE  outLC_param(
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `outLC` varchar(20) COLLATE latin1_general_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci;

CREATE TABLE  param (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `pcorProfile` varchar(100) COLLATE latin1_general_ci,
  `version` varchar(30) COLLATE latin1_general_ci,
  `wSize` int(11) NOT NULL,
  `wStep` int(11) NOT NULL,
  `kernelType_id` int(11) NOT NULL,
  `customKern` varchar(100) COLLATE latin1_general_ci,
  `kernelSigma` int(11) NOT NULL,
  `kernelShift` int(11) NOT NULL,
  `complFg_id` int(11) NOT NULL,
  `na` tinyint(1) NOT NULL,
  `bin` int(11) NOT NULL,
  `bpType_id` int(11) NOT NULL,
  `flankSize` int(11) NOT NULL,
  `noiseLevel` int(11) NOT NULL,
  `maxNA` int(11) NOT NULL,
  `maxZero` int(11) NOT NULL,
  `nShuffle` int(11) NOT NULL,
  `threshold` int(11) NOT NULL,
  `lcFDR` int(11) NOT NULL,
  `outChrom` tinyint(1) NOT NULL,
  `intervals_id` int(11) NOT NULL,
  `outLC_id` int(11) NOT NULL,
  `writeDistr` tinyint(1) NOT NULL,
  `Distances` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `version_key` (`version`),
  CONSTRAINT `kernel_type_fk` FOREIGN KEY (`kernelType_id`) REFERENCES `kernelType_param` (`id`),
  CONSTRAINT `compl_fg_fk` FOREIGN KEY (`complFg_id`) REFERENCES `complFg_param` (`id`),
  CONSTRAINT `bp_type_fk` FOREIGN KEY (`bpType_id`) REFERENCES `bpType_param` (`id`),
  CONSTRAINT `intervals_fk` FOREIGN KEY (`intervals_id`) REFERENCES `intervals_param` (`id`),
  CONSTRAINT `outLC_fk` FOREIGN KEY (`outLC_id`) REFERENCES `outLC_param` (`id`)
  ) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci;


CREATE TABLE  mark (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `mark` varchar(100) COLLATE latin1_general_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `mark` (`mark`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci;


CREATE TABLE  lab (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `lab` varchar(20) COLLATE latin1_general_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `lab` (`lab`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci;




CREATE TABLE  sample (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sample` varchar(100) COLLATE latin1_general_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `sample` (`sample`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci;



CREATE TABLE  tissue (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tissue` varchar(100) COLLATE latin1_general_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `tissue` (`tissue`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci;


CREATE TABLE devstage (
  `id` INTEGER  NOT NULL AUTO_INCREMENT,
  `devstage` VARCHAR(100)  COLLATE latin1_general_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `devstage` (`devstage`)
)
ENGINE = InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci;

CREATE TABLE track_path (
  `id` INTEGER  NOT NULL AUTO_INCREMENT,
  `track_path` VARCHAR(300)  COLLATE latin1_general_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `track_path_unique` (`track_path`)
)
ENGINE = InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci;


CREATE TABLE confounder (
  `id` INT NOT NULL AUTO_INCREMENT,
  `confounder_name` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`id`)
  )
  ENGINE = InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci;

CREATE TABLE confounder_member (
  `id` INT NOT NULL AUTO_INCREMENT,
  `confounder_id` INT NOT NULL,
  `member_name` VARCHAR(100) NOT NULL,
  `member_path_id` INT NOT NULL,
  `eigen_value` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `conf_key_idx` (`confounder_id` ASC),
  CONSTRAINT `member_confounder_key` FOREIGN KEY (`confounder_id`) REFERENCES `confounder` (`id`), 
  CONSTRAINT `member_path_key` FOREIGN KEY (`member_path_id`) REFERENCES `track_path` (`id`) 
  )
  ENGINE = InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci;


CREATE TABLE  track (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `track_name` VARCHAR(200)  COLLATE latin1_general_ci NOT NULL,
  `tissue_id` int(11) DEFAULT NULL,
  `mark_id` int(11) NOT NULL,
  `sample_id` int(11) DEFAULT NULL,
  `lab_id` int(11) DEFAULT NULL,
  `devstage_id` int(11) DEFAULT NULL,
  `track_path_id`  int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_tissue` (`tissue_id`),
  KEY `fk_mark` (`mark_id`),
  KEY `fk_sample` (`sample_id`),
  KEY `fk_lab` (`lab_id`),
  KEY `fk_devstage` (`devstage_id`),
  KEY `fk_track_path` (`track_path_id`),
  UNIQUE KEY `track_name_unique` (`track_name`, `track_path_id`),
  CONSTRAINT `fk_devstage` FOREIGN KEY (`devstage_id`) REFERENCES `devstage` (`id`),
  CONSTRAINT `fk_lab` FOREIGN KEY (`lab_id`) REFERENCES `lab` (`id`),
  CONSTRAINT `fk_mark` FOREIGN KEY (`mark_id`) REFERENCES `mark` (`id`),
  CONSTRAINT `fk_sample` FOREIGN KEY (`sample_id`) REFERENCES `sample` (`id`),
  CONSTRAINT `fk_tissue` FOREIGN KEY (`tissue_id`) REFERENCES `tissue` (`id`),
  CONSTRAINT `fk_track_path` FOREIGN KEY (`track_path_id`) REFERENCES `track_path` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci;


CREATE TABLE  org (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `org` varchar(100) COLLATE latin1_general_ci NOT NULL,
  `assembly` varchar(100) COLLATE latin1_general_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `org` (`org`,`assembly`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci;

CREATE TABLE  run (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `track1_id` int(11) NOT NULL,
  `track2_id` int(11) NOT NULL,
  `param_id` int(11) NOT NULL,
  `prog_run_id` varchar(20) COLLATE latin1_general_ci NOT NULL,
  `confounder_id` int(11) DEFAULT NULL,
  `nFgr` int(11) NOT NULL,
  `nBkg` int(11) NOT NULL,
  `Fg_Corr` float NOT NULL,  
  `Fg_av_Corr` float NOT NULL,  
  `FgCorr_sd` float NOT NULL,
  `Bg_Corr` float NOT NULL,
  `Bg_av_Corr` float NOT NULL,
  `BgCorr_sd` float NOT NULL,
  `mann_z` float NOT NULL,
  `p_value` double NOT NULL,
  `date` varchar(100) COLLATE latin1_general_ci NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_track1` (`track1_id`),
  KEY `fk_track2` (`track2_id`),
  KEY `fk_param` (`param_id`),
  UNIQUE KEY `run_unique` (`track1_id`, `track2_id`, `param_id`),
  CONSTRAINT `fk_param` FOREIGN KEY (`param_id`) REFERENCES `param` (`id`),
  CONSTRAINT `fk_track1` FOREIGN KEY (`track1_id`) REFERENCES `track` (`id`),
  CONSTRAINT `fk_track2` FOREIGN KEY (`track2_id`) REFERENCES `track` (`id`),
  CONSTRAINT `fk_confounder` FOREIGN KEY (`confounder_id`) REFERENCES `confounder` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci;



CREATE TABLE  bkg (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `run_id` int(11) NOT NULL,
  `bkg_corr` mediumtext COLLATE latin1_general_ci NOT NULL,
  `bkg_dist_corr` text COLLATE latin1_general_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `run_unique` (`run_id`),
  CONSTRAINT `run_fk_constraint` FOREIGN KEY (`run_id`) REFERENCES `run` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci;



CREATE TABLE  chrom (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `chrom` varchar(40) COLLATE latin1_general_ci NOT NULL,
  `org_id` int(11) NOT NULL,
  `size` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `chrom_uniq` (`org_id`,`chrom`),
  KEY `org_fk_constraint` (`org_id`),
  CONSTRAINT `org_fk_constraint` FOREIGN KEY (`org_id`) REFERENCES `org` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci;


CREATE TABLE  fg (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `chrom_id` int(11) NOT NULL,
  `corr` text COLLATE latin1_general_ci NOT NULL,
  `run_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `run_unique` (`run_id`, `chrom_id`),
  KEY `chrom_corr_fk` (`chrom_id`),
  CONSTRAINT `chrom_corr_fk` FOREIGN KEY (`chrom_id`) REFERENCES `chrom` (`id`),
  CONSTRAINT `run_corr_fk` FOREIGN KEY (`run_id`) REFERENCES `run` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci;

CREATE TABLE  dist_corr (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `chrom_id` int(11) NOT NULL,
  `dist` int(11) NOT NULL,
  `corr` float NOT NULL,
  `run_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `run_unique` (`run_id`, `chrom_id`, `dist`),
  KEY `chrom_dist_fk` (`chrom_id`),
  CONSTRAINT `chrom_dist_fk` FOREIGN KEY (`chrom_id`) REFERENCES `chrom` (`id`),
  CONSTRAINT `run_dist_fk` FOREIGN KEY (`run_id`) REFERENCES `run` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci;




INSERT INTO bpType_param (bpType) VALUES ("SCORE");
INSERT INTO bpType_param (bpType) VALUES ("SIGNAL");
INSERT INTO bpType_param (bpType) VALUES ("LOGPVAL");

INSERT INTO complFg_param (complFg) VALUES ("IGNORE_STRAND");
INSERT INTO complFg_param (complFg) VALUES ("COLINEAR");
INSERT INTO complFg_param (complFg) VALUES ("COMPLEMENT");


INSERT INTO kernelType_param (kernel_type) VALUES ("NORMAL");
INSERT INTO kernelType_param (kernel_type) VALUES ("RIGHT_EXP");
INSERT INTO kernelType_param (kernel_type) VALUES ("LEFT_EXP");

INSERT INTO outWig_param (outWig) VALUES ("NONE");
INSERT INTO outWig_param (outWig) VALUES ("BASE");
INSERT INTO outWig_param (outWig) VALUES ("CENTER");
INSERT INTO outWig_param (outWig) VALUES ("BASE_MULT");
INSERT INTO outWig_param (outWig) VALUES ("CENTER_MULT");

INSERT INTO intervals_param (intervals) VALUES ("NONE");
INSERT INTO intervals_param (intervals) VALUES ("GENE");
INSERT INTO intervals_param (intervals) VALUES ("EXON");
INSERT INTO intervals_param (intervals) VALUES ("IVS");
INSERT INTO intervals_param (intervals) VALUES ("GENE_BEG");
INSERT INTO intervals_param (intervals) VALUES ("EXON_BEG");
INSERT INTO intervals_param (intervals) VALUES ("IVS_BEG");
INSERT INTO intervals_param (intervals) VALUES ("GENE_END");
INSERT INTO intervals_param (intervals) VALUES ("EXON_END");
INSERT INTO intervals_param (intervals) VALUES ("IVS_END");

INSERT INTO outLC_param (outLC) VALUES ("NONE");
INSERT INTO outLC_param (outLC) VALUES ("BASE");
INSERT INTO outLC_param (outLC) VALUES ("CENTER");
INSERT INTO outLC_param (outLC) VALUES ("BASE_MULT");
INSERT INTO outLC_param (outLC) VALUES ("CENTER_MULT");



