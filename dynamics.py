class Dynamics:

    def dynamics(self, psi0, H,  lista_expect=[]):
        opts = {"store_states": True}
        dynamic = mesolve(H, psi0, x, c_ops = [], e_ops = lista_expect, options=opts) 
        
        return dynamic
