

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:

        mainFolders = set(folder)
        output = []

        for path in folder:
            old_path = path
            path = path[1::].split("/")
            path.pop()

            parent = ""
            all_parents = set()

            for item in path: 
                parent += "/" + item
                all_parents.add(parent)
                
            if len(all_parents - mainFolders) < len(all_parents):
                continue
            
            output.append(old_path)
        
        return output


# class Solution:
#     def removeSubfolders(self, folder: List[str]) -> List[str]:

#         folder.sort()
#         output = [folder[0]]

#         for i in range(1, len(folder)):

#             parent = output[-1] + "/"
#             if folder[i].startswith(parent):
#                 continue
#             output.append(folder[i])

#         return output
                



      


        # mainFolders = set(folder)
        # output = []

        # for path in folder:
            
        #     old_path = path
        #     path = path[1::].split("/")
        #     path.pop()

        #     parent = ""
        #     found = False

        #     for item in path: 
        #         parent += "/" + item
        #         if parent in mainFolders:
        #             found = True
        #             break
            
        #     if not found:
        #         output.append(old_path)
        
        # return output


