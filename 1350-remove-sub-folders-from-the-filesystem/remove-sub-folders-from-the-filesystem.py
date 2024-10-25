class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:

        folder.sort()
        output = [folder[0]]

        for i in range(1, len(folder)):

            parent = output[-1] + "/"
            if folder[i].startswith(parent):
                continue
            output.append(folder[i])

        return output