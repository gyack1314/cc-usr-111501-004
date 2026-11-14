from common import unique,number
def operations(data):
    maps={r['version']:r for r in data['map_versions']};runs=unique(data['work_runs'],'run_id')
    for r in runs.values():
        if r['map_version'] not in maps or r['end']<=r['start']:raise ValueError('作业地图或时段非法')
    checks=unique(data['audits'],'audit_id')
    if any(r['run_id'] not in runs or not 0<=number(r['observed_fraction'])<=1 for r in checks.values()):raise ValueError('抽查关联或覆盖率非法')
    return {'runs':runs,'audits':checks,'takeovers':sum(r['takeover'] for r in runs.values()),'rework':sum(r['rework'] for r in runs.values())}
