CREATE TABLE  outRes_param (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `outRes` varchar(10) COLLATE latin1_general_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci;


CREATE TABLE  outWig_param (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `outWig` varchar(20) COLLATE latin1_general_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci;


CREATE TABLE  scale_param (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `scale` varchar(10) COLLATE latin1_general_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci;


CREATE TABLE  dist_output_param (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `dist_output` varchar(10) COLLATE latin1_general_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci;

CREATE TABLE  input_type_param (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `type` varchar(15) COLLATE latin1_general_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci ROW_FORMAT=DYNAMIC;

CREATE TABLE  kernel_type_param (
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

CREATE TABLE  param (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `prof_path` varchar(100) COLLATE latin1_general_ci DEFAULT NULL,
  `track_path` varchar(100) COLLATE latin1_general_ci NOT NULL,
  `res_path` varchar(100) COLLATE latin1_general_ci NOT NULL,
  `map` varchar(100) COLLATE latin1_general_ci DEFAULT NULL,
  `pcor_profile` varchar(100) COLLATE latin1_general_ci DEFAULT NULL,
  `wSize` int(11) NOT NULL DEFAULT '100000',
  `wStep` int(11) NOT NULL DEFAULT '100000',
  `kernel_type_id` int(11) NOT NULL DEFAULT '1',
  `kernel_sigma` int(11) NOT NULL DEFAULT '1000',
  `kernel_shift` int(11) NOT NULL DEFAULT '0',
  `kernel_NS` int(11) NOT NULL DEFAULT '0',
  `compl_Fg_id` int(11) NOT NULL DEFAULT '3',
  `statistics` varchar(100) COLLATE latin1_general_ci NOT NULL,
  `params_file` varchar(100) COLLATE latin1_general_ci DEFAULT './params',
  `aliases` varchar(100) COLLATE latin1_general_ci NOT NULL,
  `log` varchar(100) COLLATE latin1_general_ci NOT NULL,
  `chrom` varchar(100) COLLATE latin1_general_ci NOT NULL,
  `na` tinyint(1) DEFAULT '0',
  `input_type_id` int(11) NOT NULL DEFAULT '4',
  `strand` tinyint(1) NOT NULL DEFAULT '0',
  `scale_factor` float NOT NULL DEFAULT '0.2',
  `step` int(11) NOT NULL DEFAULT '100',
  `scale_id` int(11) DEFAULT '3',
  `lAauto` int(11) NOT NULL DEFAULT '0',
  `bpType_id` int(11) DEFAULT '1',
  `flankSize` int(11) NOT NULL DEFAULT '500',
  `noiseLevel` float NOT NULL DEFAULT '0.5',
  `maxNA` int(11) NOT NULL DEFAULT '50',
  `maxZero` int(11) NOT NULL DEFAULT '80',
  `nShuffle` int(11) NOT NULL DEFAULT '100',
  `maxShuffle` int(11) NOT NULL DEFAULT '10000',
  `mapIv` varchar(50) COLLATE latin1_general_ci DEFAULT NULL,
  `threshold` int(11) NOT NULL DEFAULT '0',
  `corrOnly` tinyint(1) NOT NULL DEFAULT '0',
  `outRes_id` int(11) DEFAULT '3',
  `outDistr` tinyint(1) NOT NULL DEFAULT '1',
  `dist_output_id` int(11) DEFAULT '2',
  `outThreshold` float NOT NULL DEFAULT '1',
  `outSpectr` tinyint(1) NOT NULL DEFAULT '0',
  `outChrom` tinyint(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `kernel_type_fk` (`kernel_type_id`),
  KEY `compl_fg_fk` (`compl_Fg_id`),
  KEY `input_type_fk` (`input_type_id`),
  KEY `bp_type_fk` (`bpType_id`),
  KEY `dist_output_fk` (`dist_output_id`)
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
  `devstage` VARCHAR(30)  NOT NULL,
  PRIMARY KEY (`id`)
)
ENGINE = InnoDB;


CREATE TABLE  track (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tissue_id` int(11) DEFAULT NULL,
  `mark_id` int(11) NOT NULL,
  `sample_id` int(11) NOT NULL,
  `lab_id` int(11) DEFAULT NULL,
  `devstage_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_tissue` (`tissue_id`),
  KEY `fk_mark` (`mark_id`),
  KEY `fk_sample` (`sample_id`),
  KEY `fk_lab` (`lab_id`),
  KEY `fk_devstage` (`devstage_id`),
  CONSTRAINT `fk_devstage` FOREIGN KEY (`devstage_id`) REFERENCES `devstage` (`id`),
  CONSTRAINT `fk_lab` FOREIGN KEY (`lab_id`) REFERENCES `lab` (`id`),
  CONSTRAINT `fk_mark` FOREIGN KEY (`mark_id`) REFERENCES `mark` (`id`),
  CONSTRAINT `fk_sample` FOREIGN KEY (`sample_id`) REFERENCES `sample` (`id`),
  CONSTRAINT `fk_tissue` FOREIGN KEY (`tissue_id`) REFERENCES `tissue` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci;


CREATE TABLE  org (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `org` varchar(100) COLLATE latin1_general_ci NOT NULL,
  `version` varchar(100) COLLATE latin1_general_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `org` (`org`,`version`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci;


CREATE TABLE  run (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `track1_id` int(11) NOT NULL,
  `track2_id` int(11) NOT NULL,
  `param_id` int(11) NOT NULL,
  `prog_run_id` varchar(20) COLLATE latin1_general_ci NOT NULL,
  `nFgr` int(11) NOT NULL,
  `Bkg_av` float NOT NULL,
  `Fg_av` float NOT NULL,
  `Bkg_sd` float NOT NULL,
  `Fg_sd` float NOT NULL,
  `tot_cor` float NOT NULL,
  `mann_z` float NOT NULL,
  `p_value` double NOT NULL,
  `pc` varchar(100) COLLATE latin1_general_ci NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_track1` (`track1_id`),
  KEY `fk_track2` (`track2_id`),
  KEY `fk_param` (`param_id`),
  CONSTRAINT `fk_param` FOREIGN KEY (`param_id`) REFERENCES `param` (`id`),
  CONSTRAINT `fk_track1` FOREIGN KEY (`track1_id`) REFERENCES `track` (`id`),
  CONSTRAINT `fk_track2` FOREIGN KEY (`track2_id`) REFERENCES `track` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci;



CREATE TABLE  bkg (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `run_id` int(11) NOT NULL,
  `bkg_corr` text COLLATE latin1_general_ci NOT NULL,
  `bkg_dist_corr` text COLLATE latin1_general_ci NOT NULL,
  PRIMARY KEY (`id`),
  KEY `run_fk_constraint` (`run_id`),
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



CREATE TABLE  chrom_stat (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `run_id` int(11) NOT NULL,
  `chrom_id` int(11) NOT NULL,
  `track1_av` float NOT NULL,
  `track2_av` float NOT NULL,
  `cc` float NOT NULL,
  `count` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `run_fk` (`run_id`),
  KEY `chrom_fk` (`chrom_id`),
  CONSTRAINT `chrom_fk` FOREIGN KEY (`chrom_id`) REFERENCES `chrom` (`id`),
  CONSTRAINT `run_fk` FOREIGN KEY (`run_id`) REFERENCES `run` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci;


CREATE TABLE  corr_fg (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `chrom_id` int(11) NOT NULL,
  `start` int(11) NOT NULL,
  `end` int(11) NOT NULL,
  `corr` float NOT NULL,
  `run_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `run_corr_fk` (`run_id`),
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
  KEY `run_dist_fk` (`run_id`),
  KEY `chrom_dist_fk` (`chrom_id`),
  CONSTRAINT `chrom_dist_fk` FOREIGN KEY (`chrom_id`) REFERENCES `chrom` (`id`),
  CONSTRAINT `run_dist_fk` FOREIGN KEY (`run_id`) REFERENCES `run` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci;



insert into input_type_param (type) values ("BED");
insert into input_type_param (type) values ("BEDGRAPH");
insert into input_type_param (type) values ("WIG");
insert into input_type_param (type) values ("UNKNOWN");

INSERT INTO scale_param(scale) VALUES('LOG');
INSERT INTO scale_param(scale) VALUES('LIN');
INSERT INTO scale_param(scale) VALUES('AUTO');

INSERT INTO bpType_param (bpType) VALUES ("SCORE");
INSERT INTO bpType_param (bpType) VALUES ("SIGNAL");
INSERT INTO bpType_param (bpType) VALUES ("LOGPVAL");

INSERT INTO outRes_param (outRes) VALUES ("XML");
INSERT INTO outRes_param (outRes) VALUES ("TAB");
INSERT INTO outRes_param (outRes) VALUES ("BOTH");
INSERT INTO outRes_param (outRes) VALUES ("NONE");

INSERT INTO dist_output_param (dist_output) VALUES ("NONE");
INSERT INTO dist_output_param (dist_output) VALUES ("TOTAL");
INSERT INTO dist_output_param (dist_output) VALUES ("DETAIL");


INSERT INTO complFg_param (complFg) VALUES ("COLINEAR");
INSERT INTO complFg_param (complFg) VALUES ("COMPLEMENT");
INSERT INTO complFg_param (complFg) VALUES ("IGNORE_STRAND");

INSERT INTO kernel_type_param (kernel_type) VALUES ("NORMAL");
INSERT INTO kernel_type_param (kernel_type) VALUES ("RIGHT_EXP");
INSERT INTO kernel_type_param (kernel_type) VALUES ("LEFT_EXP");

INSERT INTO outWig_param (outWig) VALUES ("NONE");
INSERT INTO outWig_param (outWig) VALUES ("BASE");
INSERT INTO outWig_param (outWig) VALUES ("CENTER");
INSERT INTO outWig_param (outWig) VALUES ("BASE_MULT");
INSERT INTO outWig_param (outWig) VALUES ("CENTER_MULT");
