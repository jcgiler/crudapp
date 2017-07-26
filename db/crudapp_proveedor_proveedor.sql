--
-- PostgreSQL database dump
--

-- Dumped from database version 9.6.3
-- Dumped by pg_dump version 9.6.3

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

SET search_path = public, pg_catalog;

--
-- Data for Name: proveedor_proveedor; Type: TABLE DATA; Schema: public; Owner: jcgiler
--

COPY proveedor_proveedor (id, nombre, razon_social, identificacion, cedula, genero, correo, telefono) FROM stdin;
1	Carlos Ortega Barzola	Muebleria Palito	2	009999111009991	M	carlos.ortega@mueblesa.com.ec	0987234526
7	Juan Carlos Perez	DISTSUM	1	009999111009992	M	carlos.ortega@mueblesa.com.ec	0987103629
8	Carlos Ortega Barzola	Muebleria Palito	1	0923791341	M	lrivadeneira@indualsa.com.ec	0987103629
9	Orlando Macias Peso	TAXMARE	2	009999111009934	M	taxmare21@hotmail.com	0987103634
10	Carlos Ortega Barzola	Industrias Altimar	1	009999111009991	M	lrivadeneira@indualsa.com.ec	0987103629
11	Luis Rivadeneira Quispe	Industrias Altimar	1	009999111009991	F	carlos.ortega@mueblesa.com.ec	0987103629
3	Maritza Lopez Galpe	INDUCORP S.A.	2	009999111009993	F	mlopez@inducorp.com.ec	0987102345
\.


--
-- Name: proveedor_proveedor_id_seq; Type: SEQUENCE SET; Schema: public; Owner: jcgiler
--

SELECT pg_catalog.setval('proveedor_proveedor_id_seq', 11, true);


--
-- PostgreSQL database dump complete
--

