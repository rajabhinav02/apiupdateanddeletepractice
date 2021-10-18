import configparser
import logging

import mysql.connector
from mysql.connector import Error
from utilities import custom_logging as cl

log= cl.log(logging.DEBUG)

def getconfig():
    config=configparser.ConfigParser()
    config.read("C:\\Users\\Punam\\workspace_python\\apiupdatedeletepractice\\utilities\\Properties.ini")
    return config

connset= {
    'host': getconfig()['SQL']['hostname'],
    'database': getconfig()['SQL']['database'],
    'username': getconfig()['SQL']['username'],
    'password': getconfig()['SQL']['password']
}

def getconnection():
    try:
        conn = mysql.connector.connect(**connset)
        if conn.is_connected():
            log.info("DB Connected")
            return conn
        else:
            log.error("DB NOT connected")
    except Error as e:
        log.error(e)

def getquery(gquery):
    conn = getconnection()
    cursor = conn.cursor()
    cursor.execute(gquery)
    row = cursor.fetchone()
    conn.close()
    return row

def updatequery(uquery,data):
    conn = getconnection()
    cursor = conn.cursor()
    cursor.execute(uquery,data)
    conn.commit()
    conn.close()


