from common import unique,number
def maps(data):
    rows=unique(data['map_segments'],'segment_id')
    for r in rows.values():
        if r['valid_to']<=r['valid_from'] or number(r['length_m'])<=0:raise ValueError('地图生效期或长度非法')
    for r in data['map_adjacency']:
        if r['left'] not in rows or r['right'] not in rows:raise ValueError('道路线段关系悬空')
    return {'segments':rows,'adjacency':data['map_adjacency']}
