-- RubyDB.experiments definition

CREATE TABLE `experiments` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=67 DEFAULT CHARSET=utf8mb3;

SELECT name, id
FROM RubyDB.experiments;

SELECT distinct
result_type as value,
case
	when result_type = 'Th' then 'Theory'
	when result_type = 'Proj' then 'Project'
	when result_type = 'Exp' then 'Experiment'
	else result_type end name
FROM RubyDB.limits;

-- RubyDB.limit_displays definition


SELECT id, limit_id, plot_id, color, `style`, created_at, updated_at
FROM RubyDB.limit_displays
order by 6 desc;

-- RubyDB.limit_displays definition

CREATE TABLE `limit_displays` (
  `id` int NOT NULL AUTO_INCREMENT,
  `limit_id` int DEFAULT NULL,
  `plot_id` int DEFAULT NULL,
  `color` varchar(255) DEFAULT 'k',
  `style` varchar(255) DEFAULT 'line',
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=24922 DEFAULT CHARSET=utf8mb3;

SELECT id, user_id, limit_id, created_at, updated_at
FROM RubyDB.limit_ownerships
order by 5 desc;

-- RubyDB.limit_ownerships definition

CREATE TABLE `limit_ownerships` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int DEFAULT NULL,
  `limit_id` int DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=864 DEFAULT CHARSET=utf8mb3;

INSERT INTO RubyDB.limit_ownerships
(user_id, limit_id, created_at, updated_at)
VALUES(0, 0, '', '');


-- RubyDB.limits definition

CREATE TABLE `limits` (
  `id` int NOT NULL AUTO_INCREMENT,
  `spin_dependency` varchar(255) DEFAULT NULL,
  `result_type` varchar(255) DEFAULT 'Personal',
  `measurement_type` varchar(60) DEFAULT NULL,
  `nomhash` longblob,
  `x_units` varchar(255) DEFAULT 'GeV',
  `y_units` varchar(255) DEFAULT 'cm^2',
  `x_rescale` varchar(255) DEFAULT '1',
  `y_rescale` varchar(255) DEFAULT '1',
  `default_color` varchar(255) DEFAULT 'Blk',
  `default_style` varchar(255) DEFAULT 'Line',
  `data_values` mediumtext,
  `data_label` varchar(255) DEFAULT NULL,
  `file_name` varchar(255) DEFAULT NULL,
  `data_comment` varchar(255) DEFAULT NULL,
  `data_reference` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `creator_id` int DEFAULT NULL,
  `experiment` varchar(255) DEFAULT NULL,
  `rating` int DEFAULT '0',
  `date_of_announcement` date DEFAULT NULL,
  `public` tinyint(1) DEFAULT '0',
  `official` tinyint(1) DEFAULT '0',
  `date_official` date DEFAULT NULL,
  `greatest_hit` tinyint(1) DEFAULT '0',
  `date_of_run_start` date DEFAULT NULL,
  `date_of_run_end` date DEFAULT NULL,
  `year` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1120 DEFAULT CHARSET=utf8mb3;

INSERT INTO RubyDB.limits
(spin_dependency, result_type, measurement_type, nomhash, x_units, y_units, x_rescale, y_rescale, default_color, default_style, data_values, data_label, file_name, data_comment, data_reference, created_at, updated_at, creator_id, experiment, rating, date_of_announcement, public, official, date_official, greatest_hit, date_of_run_start, date_of_run_end, `year`)
VALUES('', 'Personal', '', ?, 'GeV', 'cm^2', '1', '1', 'Blk', 'Line', '', '', '', '', '', '', '', 0, '', 0, '', 0, 0, '', 0, '', '', 0);

-- RubyDB.plot_ownerships definition

CREATE TABLE `plot_ownerships` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int DEFAULT NULL,
  `plot_id` int DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4669 DEFAULT CHARSET=utf8mb3;

INSERT INTO RubyDB.plot_ownerships
(user_id, plot_id, created_at, updated_at)
VALUES(0, 0, '', '');


-- RubyDB.plots definition

CREATE TABLE `plots` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `x_min` varchar(255) DEFAULT '1',
  `x_max` varchar(255) DEFAULT '10000',
  `y_min` varchar(255) DEFAULT '-54',
  `y_max` varchar(255) DEFAULT '-26',
  `x_units` varchar(255) DEFAULT 'GeV/c^2',
  `y_units` varchar(255) DEFAULT 'cm2',
  `user_id` int DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `plot_png` mediumblob,
  `legend_png` mediumblob,
  `plot_eps` mediumblob,
  `legend_eps` mediumblob,
  `no_id` tinyint(1) DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4669 DEFAULT CHARSET=utf8mb3;


INSERT INTO RubyDB.plots
(name, x_min, x_max, y_min, y_max, x_units, y_units, user_id, created_at, updated_at, plot_png, legend_png, plot_eps, legend_eps, no_id)
VALUES('', '1', '10000', '-54', '-26', 'GeV/c^2', 'cm2', 0, '', '', ?, ?, ?, ?, 0);

SELECT id, login, email, crypted_password, salt, created_at, updated_at, remember_token, remember_token_expires_at, reset_password_code, reset_password_code_until, activation_code, activated_at
FROM RubyDB.users
order by 6 desc;

DELETE FROM RubyDB.users;


SELECT id, `key`, value, created_at, updated_at
FROM RubyDB.simple_captcha_data;

DELETE FROM RubyDB.simple_captcha_data;

