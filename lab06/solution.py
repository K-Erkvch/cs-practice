def count_by_extension(paths: list[str]) -> dict[str, int]:
    counts = {}
    for path in paths:
        filename = path.split('/')[-1] 
        
        if '.' in filename:
            ext = filename.rsplit('.', 1)[-1].lower()
        else:
            ext = ""
            
        counts[ext] = counts.get(ext, 0) + 1
    return counts

def deepest_path(paths: list[str]) -> str:
    if not paths:
        return ""
 
    sorted_paths = sorted(paths)
    return max(sorted_paths, key=lambda p: p.count('/'))