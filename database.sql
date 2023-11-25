--
-- PostgreSQL database dump
--

-- Dumped from database version 15.4
-- Dumped by pg_dump version 15.4

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: friendship; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.friendship (
    id_friend1 character varying(36) NOT NULL,
    id_friend2 character varying(36) NOT NULL,
    friendssince date DEFAULT CURRENT_TIMESTAMP
);


ALTER TABLE public.friendship OWNER TO postgres;

--
-- Name: recycling; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.recycling (
    id character varying(36) NOT NULL,
    id_user character varying(36),
    recycle_date date DEFAULT CURRENT_TIMESTAMP NOT NULL,
    allocated_points integer NOT NULL
);


ALTER TABLE public.recycling OWNER TO postgres;

--
-- Name: users; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.users (
    id character varying(36) NOT NULL,
    last_name character varying(20) NOT NULL,
    first_name character varying(50) NOT NULL,
    username character varying(30) NOT NULL,
    email character varying(50) NOT NULL,
    password character varying(60) NOT NULL,
    total_points bigint DEFAULT 0
);


ALTER TABLE public.users OWNER TO postgres;

--
-- Data for Name: friendship; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.friendship (id_friend1, id_friend2, friendssince) FROM stdin;
\.


--
-- Data for Name: recycling; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.recycling (id, id_user, recycle_date, allocated_points) FROM stdin;
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.users (id, last_name, first_name, username, email, total_points) FROM stdin;
\.


--
-- Name: friendship friendship_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.friendship
    ADD CONSTRAINT friendship_pkey PRIMARY KEY (id_friend1, id_friend2);


--
-- Name: recycling recycling_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.recycling
    ADD CONSTRAINT recycling_pkey PRIMARY KEY (id);


--
-- Name: users users_email_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_email_key UNIQUE (email);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- Name: users users_username_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_username_key UNIQUE (username);


--
-- Name: recycling recycling_id_user_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.recycling
    ADD CONSTRAINT recycling_id_user_fkey FOREIGN KEY (id_user) REFERENCES public.users(id);


--
-- PostgreSQL database dump complete
--