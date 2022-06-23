# 📊 1. Úkol na IOS - VUT

Hodnocení: 12/15

### Výstup z hodnotících testů
```
12:celkem bodu za projekt
#-- automaticke hodnoceni -----------------------------
0:ok: docasne soubory:
0.2:ok: prázdný stdin
0:test03_cat1: opis vstupniho souboru na vystup
# ./corona test.csv <stdin >>stdout 2>>stderr; echo $? >>errcode
# diff -u stdout.ref stdout
#   --- stdout.ref
#   +++ stdout
#   @@ -1,6 +1,6 @@
#    5306034f-df10-4d10-95bf-7295a464d36c,2021-03-17,45,M,CZ072,CZ0723,,,1
#    5bc70890-eb96-4c53-b839-15a53a01dcfa,2021-11-12,83,Z,CZ064,CZ0647,,,1
#    9ac242d6-0440-4e2e-bd07-a960fafab5b8,2021-11-02,10,M,CZ010,CZ0100,,,1
#   +\nfdf0ebad-9123-4d58-8961-96ce585b384a,2022-02-04,32,Z,CZ032,CZ0323,,,1
#    dd2f91db-5866-4902-9332-2d3b384b2820,2021-11-24,72,M,CZ010,CZ0100,,,1
#   -fdf0ebad-9123-4d58-8961-96ce585b384a,2022-02-04,32,Z,CZ032,CZ0323,,,1
#    id,datum,vek,pohlavi,kraj_nuts_kod,okres_lau_kod,nakaza_v_zahranici,nakaza_zeme_csu_kod,reportovano_khs
0:test04_cat2: opis vice vstupnich souboru na vystup
# ./corona test1.csv test2.csv test3.csv <stdin >>stdout 2>>stderr; echo $? >>errcode
# diff -u stdout.ref stdout
#   --- stdout.ref
#   +++ stdout
#   @@ -1,4 +1,2 @@
#   -5e34346e-05c9-464f-8c24-89344e3325ce,2021-02-12,6,M,CZ032,CZ0326,,,1
#   -777a3ad9-507a-4018-b905-20918c4cc8b8,2021-02-04,50,M,CZ053,CZ0532,,,1
#   -dbf75bc0-8625-4284-b8c5-852fb8e4e8fa,2021-12-16,73,Z,CZ051,CZ0513,,,1
#   +\ndbf75bc0-8625-4284-b8c5-852fb8e4e8fa,2021-12-16,73,Z,CZ051,CZ0513,,,1\n5e34346e-05c9-464f-8c24-89344e3325ce,2021-02-12,6,M,CZ032,CZ0326,,,1\n777a3ad9-507a-4018-b905-20918c4cc8b8,2021-02-04,50,M,CZ053,CZ0532,,,1
#    id,datum,vek,pohlavi,kraj_nuts_kod,okres_lau_kod,nakaza_v_zahranici,nakaza_zeme_csu_kod,reportovano_khs
0:test05_cat3: opis vice vstupnich souboru vcetne gz na vystup
# ./corona test1.csv test2.csv.gz test3.csv.gz <stdin >>stdout 2>>stderr; echo $? >>errcode
# diff -u stdout.ref stdout
#   --- stdout.ref
#   +++ stdout
#   @@ -1,4 +1,2 @@
#   -23a99fc0-b0c9-44a1-8408-4de0fa4e23f1,2020-11-20,45,Z,CZ032,CZ0325,,,1
#   -719c2120-5114-4209-860e-983d1b442042,2021-02-22,45,Z,CZ010,CZ0100,,,1
#   -7a61060c-deec-4bd8-82fb-3b22eda0f29e,2020-11-03,53,Z,CZ010,CZ0100,,,1
#   +\n719c2120-5114-4209-860e-983d1b442042,2021-02-22,45,Z,CZ010,CZ0100,,,1\n7a61060c-deec-4bd8-82fb-3b22eda0f29e,2020-11-03,53,Z,CZ010,CZ0100,,,1\n23a99fc0-b0c9-44a1-8408-4de0fa4e23f1,2020-11-20,45,Z,CZ032,CZ0325,,,1
#    id,datum,vek,pohlavi,kraj_nuts_kod,okres_lau_kod,nakaza_v_zahranici,nakaza_zeme_csu_kod,reportovano_khs
0.4:ok: opis stdin na stdout
0:test07_cmd_merge: prikaz merge
# ./corona merge test1.csv test2.csv <stdin >>stdout 2>>stderr; echo $? >>errcode
# diff -u stdout.ref stdout
#   --- stdout.ref
#   +++ stdout
#   @@ -1,5 +1,4 @@
#   -0017cda0-5726-498a-93c0-0692e11604e1,2022-02-08,17,Z,CZ064,CZ0645,,,1
#   -41495b6a-1459-40b2-b40f-bd50d72061b4,2020-11-23,54,Z,CZ064,CZ0645,,,1
#   -50eaa633-404b-4753-9918-c7a8ecef6b00,2021-01-07,32,M,CZ010,CZ0100,,,1
#   +50eaa633-404b-4753-9918-c7a8ecef6b00,2021-01-07,32,M,CZ010,CZ0100,,,1\n0017cda0-5726-498a-93c0-0692e11604e1,2022-02-08,17,Z,CZ064,CZ0645,,,1
#    5dfb742b-767d-4de6-acf1-008b46dde9db,2022-01-20,24,M,CZ010,CZ0100,,,1
#   +\n41495b6a-1459-40b2-b40f-bd50d72061b4,2020-11-23,54,Z,CZ064,CZ0645,,,1
#    id,datum,vek,pohlavi,kraj_nuts_kod,okres_lau_kod,nakaza_v_zahranici,nakaza_zeme_csu_kod,reportovano_khs
0.5:ok: prikaz infected
0:test09_cmd_infected_err: prikaz infected s invalid záznamy
# ./corona infected test.csv <stdin >>stdout 2>>stderr; echo $? >>errcode
# diff -u stderr.ref stderr
#   --- stderr.ref
#   +++ stderr
#   @@ -3,4 +3,4 @@
#    Invalid age: 92ae740e-fdb2-431c-a9c7-fe2b591fe842,2022-01-13,N,M,CZ010,CZ0100,,,1
#    Invalid date: 4bb6cd35-962f-4aa1-92ec-39fb18f6f8d9,yesterday,30,M,CZ071,CZ0712,,,1
#    Invalid date: 4bfa23de-9395-45e0-b720-82e53030f08c,2022-13-32,40,Z,CZ041,CZ0411,,,1
#   -Invalid date: df1b5435-c05c-4d71-9847-e510fd1aba42,2020-02-30,26,Z,CZ071,CZ0712,,,1
#   +Invalid date: \ndf1b5435-c05c-4d71-9847-e510fd1aba42,2020-02-30,26,Z,CZ071,CZ0712,,,1
0.5:ok: prikaz gender
0.5:ok: prikaz age
0.5:ok: prikaz daily
0.5:ok: prikaz monthly
0.5:ok: prikaz yearly
0.5:ok: prikaz countries
0.5:ok: prikaz districts
0.5:ok: prikaz regions
0.8:ok: filtr -a
0:test19_filter_b: filtr -b
# ./corona -b 2022-01-01 test.csv <stdin >>stdout 2>>stderr; echo $? >>errcode
# diff -u stdout.ref stdout
#   --- stdout.ref
#   +++ stdout
#   @@ -2,6 +2,6 @@
#    390686a5-c26f-4000-a8c5-3ee98893a95b,2021-10-26,73,Z,CZ063,CZ0632,,,1
#    847d389b-3ff8-4462-b182-550120ff0cfe,2021-12-20,40,M,CZ010,CZ0100,,,1
#    9fdeb70d-7b7b-439c-ad70-ea7c89495761,2021-12-21,35,Z,CZ080,CZ0801,,,1
#   +\nbfed487b-7de6-422a-9491-b336f6bb36fd,2021-01-05,4,M,CZ031,CZ0311,,,1
#    a59385a5-bc1a-4066-a8f2-c7be0d8046fe,2020-11-30,2,M,CZ072,CZ0721,,,1
#   -bfed487b-7de6-422a-9491-b336f6bb36fd,2021-01-05,4,M,CZ031,CZ0311,,,1
#    id,datum,vek,pohlavi,kraj_nuts_kod,okres_lau_kod,nakaza_v_zahranici,nakaza_zeme_csu_kod,reportovano_khs
0.8:ok: filtr -ab
0:test21_filter_g: filtr -g
# ./corona -g Z test.csv <stdin >>stdout 2>>stderr; echo $? >>errcode
# diff -u stdout.ref stdout
#   --- stdout.ref
#   +++ stdout
#   @@ -2,6 +2,6 @@
#    4ef2c983-0cee-4885-b713-a9370ea77c0d,2021-01-29,50,Z,CZ031,CZ0313,,,1
#    55914e16-481c-4acf-9a2c-b2c386650601,2021-02-07,18,Z,CZ080,CZ0806,,,1
#    6050dfc7-c2be-447b-a556-b7682b57aa52,2021-02-18,50,Z,CZ051,CZ0513,,,1
#   -dea9862f-c06d-47a4-a19b-6b54fe905d8d,2020-10-31,65,Z,CZ031,CZ0314,,,1
#   +\ndea9862f-c06d-47a4-a19b-6b54fe905d8d,2020-10-31,65,Z,CZ031,CZ0314,,,1
#    e98b69de-da81-4883-be41-b2a900582848,2021-12-20,7,Z,CZ053,CZ0532,,,1
#    id,datum,vek,pohlavi,kraj_nuts_kod,okres_lau_kod,nakaza_v_zahranici,nakaza_zeme_csu_kod,reportovano_khs
0.8:ok: filtr -abg
0.75:ok: combo -abg infected
0.75:ok: combo -g daily
1.0:ok: graph -s countries
1.0:ok: graph -s width gender
0.5:ok: graph -s width gender -- floating point math
0:test28_bonus_d_districts: bonus -d districts
# ./corona -d okresy.csv districts test.csv <stdin >>stdout 2>>stderr; echo $? >>errcode
# diff -u stdout.ref stdout
#   --- stdout.ref
#   +++ stdout
#   @@ -1,10 +1,10 @@
#   -Ceske Budejovice  : 5
#   -Frydek-Mistek     : 2
#   -Hlavni mesto Praha: 2
#   -Kromeriz          : 2
#   -Olomouc           : 2
#   -Opava             : 1
#   -Praha-vychod      : 1
#   -Pribram           : 1
#   -Rakovnik          : 1
#   -Usti nad Orlici   : 2
#   +CZ0100: 2
#   +CZ0209: 1
#   +CZ020B: 1
#   +CZ020C: 1
#   +CZ0311: 5
#   +CZ0534: 2
#   +CZ0712: 2
#   +CZ0721: 2
#   +CZ0802: 2
# Vypis byl zkracen, cely text viz test28_bonus_d_districts/hodnoceni-auto
0:test29_bonus_r_regions: bonus -r regions
# ./corona -r kraje.csv regions test.csv <stdin >>stdout 2>>stderr; echo $? >>errcode
# diff -u stdout.ref stdout
#   --- stdout.ref
#   +++ stdout
#   @@ -1,7 +1,7 @@
#   -Hlavni mesto Praha  : 2
#   -Jihocesky kraj      : 5
#   -Moravskoslezsky kraj: 3
#   -Olomoucky kraj      : 2
#   -Pardubicky kraj     : 2
#   -Stredocesky kraj    : 3
#   -Zlinsky kraj        : 2
#   +CZ010: 2
#   +CZ020: 3
#   +CZ031: 5
#   +CZ053: 2
#   +CZ071: 2
#   +CZ072: 2
#   +CZ080: 3
0:test30_bonus_r_regions_err: bonus -r regions s invalid záznamy
# ./corona -r kraje.csv regions test.csv <stdin >>stdout 2>>stderr; echo $? >>errcode
# diff -u stdout.ref stdout
#   --- stdout.ref
#   +++ stdout
#   @@ -1,7 +1,9 @@
#   -Hlavni mesto Praha  : 1
#   -Jihocesky kraj      : 5
#   -Moravskoslezsky kraj: 3
#   -Olomoucky kraj      : 2
#   -Pardubicky kraj     : 2
#   -Stredocesky kraj    : 2
#   -Zlinsky kraj        : 2
#   +42: 1
#   +CZ010: 1
#   +CZ020: 2
#   +CZ031: 5
#   +CZ053: 2
#   +CZ071: 2
#   +CZ072: 2
#   +CZ080: 3
#   +CZ999: 1
# diff -u stderr.ref stderr
#   --- stderr.ref
#   +++ stderr
# Vypis byl zkracen, cely text viz test30_bonus_r_regions_err/hodnoceni-auto
#------------------------------------------------------
11.5:celkove score (max pro hodnoceni 15)
12:celkem bodu za projekt
```
