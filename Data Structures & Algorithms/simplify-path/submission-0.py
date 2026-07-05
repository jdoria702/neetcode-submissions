class Solution:
    def simplifyPath(self, path: str) -> str:
        """
        Go character by character building the file path name
            - If file path is "..", pop directory from stack if exists
            - Ignore cases of "/" (empty string) or "."
            - Else, append current directory to the stack

        """
        stack = []
        curr = ""

        for ch in path + "/":
            if ch == "/":

                # Pop from stack
                if curr == "..":
                    if stack:
                        stack.pop()

                # Completed building the directory
                # or
                # Ignore multiple "/" or current directory
                elif curr != "" and curr != ".":
                    stack.append(curr)
                
                curr = ""

            else:
                curr = curr + ch

        return "/" + "/".join(stack)