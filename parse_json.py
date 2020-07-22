#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xml.etree.cElementTree as ET
import pprint
import re
import codecs
import json

SAMPLE_FILE = "/Users/fabriciomattos/Documents/udacity/mongo_db/rj.osm"

#lower = re.compile(r'^([a-z]|_)*$')
lower_colon = re.compile(r'^([a-z]|_)*:([a-z]|_)*$')
#problemchars = re.compile(r'[=\+/&<>;\'"\?%#$@\,\. \t\r\n]')

CREATED = [ "version", "changeset", "timestamp", "user", "uid"]

VERSION=[":af" ,
":am",
":an",
":ar",
":az",
":ba",
":be",
":bg",
":bn",
":bo",
":br",
":bs",
":ca",
":ce",
":co",
":cs",
":cv",
":cy",
":da",
":de",
":el",
":en",
":eo",
":es",
":et",
":eu",
":fa",
":fi",
":fj",
":fo",
":fr",
":fy",
":ga",
":gd",
":gl",
":gn",
":ha",
":he",
":hi",
":hr",
":hu",
":hy",
":ia",
":id",
":ie",
":io",
":is",
":it",
":ja",
":jv",
":ka",
":kk",
":kn",
":ko",
":ku",
":kw",
":ky",
":la",
":lb",
":li",
":lt",
":lv",
":mi",
":mk",
":ml",
":mn",
":mr",
":ms",
":my",
":na",
":ne",
":nl",
":nn",
":no",
":oc",
":os",
":pa",
":pl",
":pt",
":qu",
":rm",
":ro",
":ru",
":sc",
":sh",
":sk",
":sl",
":sq",
":sr",
":su",
":sv",
":sw",
":ta",
":tg",
":th",
":tk",
":tl",
":tr",
":tt",
":tw",
":ug",
":uk",
":ur",
":uz",
":vi",
":vo",
":yi",
":yo",
":zh",
":hc",
":te"]


def shape_element(element):
    node = {}
    if element.tag == "node" or element.tag == "way" :
       node = {}
    node["created"]={}
    node["address"]={}
    node["pos"]=[]
    refs=[]

    if element.tag == "node" or element.tag == "way" :
        if "id" in element.attrib:
            node["id"]=element.attrib["id"]
        node["type"]=element.tag

        if "visible" in element.attrib.keys():
            node["visible"]=element.attrib["visible"]

        for elem in CREATED:
            if elem in element.attrib:
                node["created"][elem]=element.attrib[elem]
        if "lat" in element.attrib:
            node["pos"].append(float(element.attrib["lat"]))
        if "lon" in element.attrib:
            node["pos"].append(float(element.attrib["lon"]))

        for tag in element.iter("tag"):
            
            if tag.attrib['k'] == "addr:housenumber":
                node["address"]["housenumber"]=tag.attrib['v']
            if tag.attrib['k'] == "addr:postcode":
                    node["address"]["postcode"]=tag.attrib['v']
            if tag.attrib['k'] == "addr:street":
                    node["address"]["street"]=tag.attrib['v']
            if tag.attrib['k'] == "addr:city":
                node["address"]["city"]=tag.attrib['v'] 
            if tag.attrib['k'] == "addr:country":
                node["address"]["country"]=tag.attrib['v'] 
            #if tag.attrib['k'].find("addr")==-1:
            #        node[tag.attrib['k']]=tag.attrib['v']
            if  not tag.attrib['k'][-3:] in VERSION and not tag.attrib['k'].startswith("addr:"):
                node[tag.attrib['k']]=tag.attrib['v']
            

        for nd in element.iter("nd"):
             refs.append(nd.attrib["ref"])
        if node["address"] =={}:
            node.pop("address", None)
        if refs != []:
           node["node_refs"]=refs
        return node
    else:

        return None


def process_map(file_in, pretty = False):
    # You do not need to change this file
    file_out = "{0}.json".format(file_in)
    data = []
    with codecs.open(file_out, "w",'utf-8') as fo:
        for _, element in ET.iterparse(file_in):
            el = shape_element(element)
            if el:
                data.append(el)
                
        json.dump(data,fo,indent=4,sort_keys=False)

    return data

process_map(SAMPLE_FILE)


