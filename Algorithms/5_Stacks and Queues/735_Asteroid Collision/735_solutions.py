#20260917
class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack=[]
        for i in range(len(asteroids)):
            if not stack:
                stack.append(asteroids[i])
            else:
                disappeared=False
                while stack:
                    if stack[-1]>0 and asteroids[i]<0:
                        if stack[-1]>-asteroids[i]:#消失了，不能塞
                            disappeared=True
                            break
                        elif stack[-1]==-asteroids[i]:#消失了，不能塞
                            stack.pop()
                            disappeared=True
                            break
                        elif stack[-1]<-asteroids[i]:#没消失
                            stack.pop()
                    else:
                        break
                if disappeared==False:
                    stack.append(asteroids[i])
        return stack
