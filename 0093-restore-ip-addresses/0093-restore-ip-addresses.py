class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ret = []
        def gen_ip(par , st , n):
            #print("Paren = {} st = {} n = {}".format(par,st,n))
            m = len(st)
            if m < n:
                #print("String End")
                return
            elif m == n:
                out = ''
                for i in range(n-1):
                    out = out + st[i]+"."
                    #print("Out = ",out)
                out = out + st[n-1]
                if par:
                    ret.append(par + "." + out)
                else:
                    ret.append(out)
                return 
            elif n >= 2:
                cur_val = 0
                itr_len = m-(n-1)
                if itr_len > 3: itr_len = 3
                for i in range(itr_len):
                    cur_val = cur_val * 10 + int(st[i])
                    if cur_val == 0:
                        if par :
                            gen_ip(par +"." + str(cur_val),st[i+1:],n-1)
                        else:
                            gen_ip(par + str(cur_val),st[i+1:],n-1)
                        break
                    if cur_val <= 255:
                        #print("parent {} Calling Func {}".format(par,len(st[i:]) ))
                        if par :
                            gen_ip(par +"." + str(cur_val),st[i+1:],n-1)
                        else:
                            gen_ip(par + str(cur_val),st[i+1:],n-1)
                            
                        
                return
            else:
                cur_val = 0
                for i in range(m):
                    cur_val = cur_val * 10 + int(st[i])
                    if cur_val == 0 and i!= m-1:
                        return
                if cur_val <= 255 :
                    ret.append(par + "."+str(cur_val))
                
            
        gen_ip('',s,4)
        return ret
                    
                    
                
                
        