#coding=utf-8
 



from django.db import models
"""""
"dataSet":{
      "name":"chazuo",
      "XXxx":"82",
      "osType":"mac",
      "currSpeed":"86",
      "currSlope":"86",
      "sumTime":"86",
      "sumDistance":"86",
      "sumCalories":"86",
      "currRate":"86"
      
#      ���搴�璁惧��淇℃��(璁惧��->������)
chazuo,81,mac,���楂����搴�锛����浣����搴�锛����搴����浣�锛�0锛������� 1锛���遍��锛�锛�
��″害��婚��锛�姘村钩��″害锛�绱�璁￠��绋�锛�uuid

��峰��杩���ㄥ�ㄦ��璁惧��褰����杩���ㄥ�����

"""
"""
# Create your models here.
class runEvent(models.Model):
    name = models.CharField(max_length=50)
    mac=models.IPAddressField()#IPAddressField()
    osType = models.CharField(max_length=5)
    currSpeed = models.CharField(max_length=5)
    currSlope = models.CharField(max_length=6) 
    sumTime=models.CharField(max_length=10) 
    sumDistance = models.CharField(max_length=10) 
    currRate = models.CharField(max_length=10)
    sportTime=models.TimeField() 
    
  ��ㄦ�疯�����
涓�浜哄�烘��璧����锛�浼����缂���� �����哄�风�� ��电О ��у�� 骞撮�� ���搴� ���绠� 涓�浜鸿�存�� 韬�楂� 浣���� ��稿�� �����ワ��
class runerInfo(models.Model):
    name = models.CharField(max_length=50)
    mac=models.IPAddressField()#IPAddressField()
    osType = models.CharField(max_length=5)
    currSpeed = models.CharField(max_length=5)
    currSlope = models.CharField(max_length=6) 
    sumTime=models.CharField(max_length=10) 
    sumDistance = models.CharField(max_length=10) 
    currRate = models.CharField(max_length=10)
    sportTime=models.TimeField()   
create table wocustinfo   ( tizhong  smallint ,   userid  integer not null unique ,   xingbie  smallint ,   shengao  smallint ,   nicheng  varchar(60) ,   nianling  varchar(8) ,   gexingqianming  varchar(100) ,   );    
"""


SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: wousers; Type: TABLE; Schema: public; Owner: postsql; Tablespace: 
--
终端存储的输出
CREATE TABLE wousers (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    username character varying(30) NOT NULL
     );


ALTER TABLE wousers OWNER TO walk;

--
-- Name: wousers_id_seq; Type: SEQUENCE; Schema: public; Owner: postsql
--

CREATE SEQUENCE wousers_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE wousers_id_seq OWNER TO walk;

--
-- Name: wousers_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postsql
--

ALTER SEQUENCE wousers_id_seq OWNED BY wousers.id;


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postsql
--

ALTER TABLE ONLY wousers ALTER COLUMN id SET DEFAULT nextval('wousers_id_seq'::regclass);


--
-- Name: wousers_pkey; Type: CONSTRAINT; Schema: public; Owner: postsql; Tablespace: 
--

ALTER TABLE ONLY wousers
    ADD CONSTRAINT wousers_pkey PRIMARY KEY (id);


--
-- Name: wousers_username_key; Type: CONSTRAINT; Schema: public; Owner: postsql; Tablespace: 
--

ALTER TABLE ONLY wousers
    ADD CONSTRAINT wousers_username_key UNIQUE (username);

 

