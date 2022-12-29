let dfs g r =
    let n = Array.length g in
    let visited = Array.make n false in
    let rec aux v =
        if not visited.(v) then (
            visited.(v) <- true;
            List.iter aux g.(v)
        ) in
    aux r
