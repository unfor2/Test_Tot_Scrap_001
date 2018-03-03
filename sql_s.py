"""
create table if not exists tbl_save_info
(
	"ID" bigint not null
		constraint tbl_save_info_pkey
			primary key,
	"Bookmaker" varchar(50) not null,
	"EventGroup" varchar(100) not null,
	"EventTime" timestamp not null,
	"Player_A" varchar(100) not null,
	"Player_B" varchar(100) not null,
	"Bet_Type" varchar(50) not null,
	"Bet_koef" numeric(10,4) not null,
	"AddDate" abstime
)
;

create table if not exists tbl_save_info_ver001
(
	"ID" serial not null
		constraint tbl_save_info_ver001_pkey
			primary key,
	"Bookmaker" varchar(50) not null,
	"SportName_original" varchar(100) not null,
	"SportName_translated" varchar(100),
	"EventGroup_original" varchar(100) not null,
	"EventGroup_translated" varchar(100),
	"EventTime" timestamp not null,
	"EventTimeStr" varchar(20) not null,
	"EventCode" varchar(100) not null,
	"Player_1_original" varchar(100) not null,
	"Player_1_translated" varchar(100),
	"Player_2_original" varchar(100),
	"Player_2_translated" varchar(100),
	"Bet_Type_original" varchar(50) not null,
	"Bet_Type_translated" varchar(50),
	"Bet_koef" numeric(10,4) not null,
	"AddDate" abstime default CURRENT_TIMESTAMP
)
;

"""