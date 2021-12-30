class Graph:
    def __init__(self,edges):
        self.edges=edges
        self.graph_dict={}
        for start,end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start]=[end]
        print(self.graph_dict)
    def get_paths(self,start,end,path=[]):
        path=path+[start]
        
        if start==end:
            return [path]
        if start not in self.graph_dict:
            return []
        paths=[]    
            
        for node in self.graph_dict[start]:
            if node not in path:
                new_paths=self.get_paths(node,end,path)
                #print(new_paths)
                for p in new_paths:
                    paths.append(p)
        return paths
        
    def get_shortest_path(self,start,end,path=[]):
        
        if start==end:
            return [start]
        if start not in self.graph_dict:
            return None
            
        paths=self.get_paths(start,end)
        for path in range(len(paths)):
            if len(paths[path]) < len(paths[path+1]):
                return paths[path]
            elif len(paths[path]) == len(paths[path+1]):
                return (paths[path],paths[path+1])
            else:
                return paths[path+1]
        
if __name__=="__main__":
    routes=[("Mumbai","Paris"),
            ("Mumbai","Dubai"),
            ("Paris","Dubai"),
            ("Paris","New York"),
            ("Dubai","New York"),
            ("New York","Toronto")]
    graph=Graph(routes)
    start="Paris"
    end="New York"
    print(f"Paths between {start} and {end} are:",graph.get_paths(start,end))
    print(f"Shortest paths between {start} and {end} are:",graph.get_shortest_path(start,end))
