#!/usr/bin/env python
# coding=UTF-8

import sys
import xlrd
import json


if len(sys.argv) != 3:
    print """
        Usage:
            1. The name of the xls file containing EventCategory, EventAction and EventLabel
            2. The name of the output csv
    """
    sys.exit(1)


wb=xlrd.open_workbook(sys.argv[1])
sh = wb.sheet_by_index(0)

click_data = {}
shown_data = {}

def parse_click(eventlabel):
    data = json.loads(eventlabel)
    cid = data.get('cid')
    otype = data.get('type')
    desc = data.get('desc')
    if otype == 'Custom' or cid is not None:
        if otype == 'Custom':
            cid_key = "CUSTOM-WIDGET,{0},{1}".format(otype, desc)
        else:
            cid_key = "{0},{1},{2}".format(cid, otype, desc.encode('ascii', 'ignore'))
        click_data[cid_key] = click_data.get(cid_key, 0) + 1


def parse_shown(eventlabel):
    data = json.loads(eventlabel)
    for item in data.get('items', []):
        cid = item.get('cid')
        otype = item.get('typ')
        desc = item.get('desc')
        if otype == 'Custom' or cid is not None:
            if otype == 'Custom':
                cid_key = "CUSTOM-WIDGET-{0},{1},{2}".format(cid, otype, desc)
            else:
                cid_key = "{0},{1},{2}".format(cid, otype, desc)
            shown_data[cid_key] = shown_data.get(cid_key, 0) + 1


for rownum in range(sh.nrows):
    category, action, label = sh.row_values(rownum)

    if action == 'Shown':
        parse_shown(label)
    elif action == 'OnClick':
        parse_click(label)

clicks = click_data.keys()
shows = shown_data.keys()
all_ads = set(clicks + shows)

with open(sys.argv[2], 'w') as oh:
    for ad in all_ads:
        click_info = click_data.get(ad, 0)
        shown_info = shown_data.get(ad, 0)

        print ad,",", shown_info,",", click_info
        oh.write("{0},{1},{2}\n".format(ad, shown_info, click_info))