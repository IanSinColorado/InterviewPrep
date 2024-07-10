class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        
        for s in path.split("/"):
            match s:
                case "":
                    if len(stack) == 0:
                        stack.append("/")
                case "..":
                    if len(stack) > 1:
                        stack.pop(0)
                case ".":
                    continue
                case _:
                    stack.append(s)

        return "/".join(stack)