class Thermal():

  def partition_function(self, H_subsystem, kT):
      Z =  (-H_subsystem/kT).expm().tr()
      return Z

  def rho_thermal(self, H_subsystem, kT, method = 'eigensytem'):

      if method == 'eigensytem':
          result = 0*qeye((H_subsystem).shape[0])
          eigen_list = H_subsystem.eigenstates()
          for i in range(len(eigen_list[0])):
              result += np.exp(-eigen_list[0][i]/kT) * eigen_list[1][i] * eigen_list[1][i].dag()
      elif method == 'expm':
          result = (-H_subsystem/kT).expm()
      else:
          print(f' Method {method} not valid')
          result = None
      return result

  def rho_thermal_norm(self, H_subsystem, kT,  method = 'eigensytem'):
      #print(H_subsystem  )
      rho = self.rho_thermal(H_subsystem, kT, method )/  self.partition_function(H_subsystem, kT)

      return rho


