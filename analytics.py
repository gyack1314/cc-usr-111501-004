"""当前资料入口；不实现统计分析目标。"""
import json
from common import read
from maps import maps
from telemetry import points
from work import operations
def prepare_sources():
    data=read()
    return {'maps': maps(data), 'points': points(data), 'operations': operations(data)}
if __name__=="__main__":print(json.dumps(prepare_sources(),ensure_ascii=False,default=str,indent=2))