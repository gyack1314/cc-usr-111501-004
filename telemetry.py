from common import unique,number
def points(data):
    out=unique(data['telemetry'],'point_id');group={}
    for r in out.values():
        if number(r['accuracy_m'])<0:raise ValueError('定位误差非法')
        group.setdefault(r['run_id'],[]).append(r)
    for rows in group.values():
        rows.sort(key=lambda r:r['at'])
        if any(b['at']<=a['at'] for a,b in zip(rows,rows[1:])):raise ValueError('同次轨迹时间不递增')
    return group
