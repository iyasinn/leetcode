"""
This feels like a set problem

everything in the original array is a potential main folder

For each element we can map it to it's parent folders
and if any of those parent folders appear, we cna delete 

We need a fast way to check subfolder
I say a subfolder is if you are in th emain set
Or if you start with a prefix

/a -> {}
/a/b -> /a 
/c/d -> /c
/c/d/e -> /c, /c/d

"""
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:

        mainFolders = set(folder)
        output = []

        for path in folder:
            old_path = path
            path = path.split("/")
            path.pop()
            path.pop(0)

            parent = ""
            all_parents = set()

            for item in path: 
                parent += "/" + item
                all_parents.add(parent)
                
            if len(all_parents - mainFolders) < len(all_parents):
                continue
            
            output.append(old_path)
        
        return output


