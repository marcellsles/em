import matplotlib.pyplot as plt
import numpy as np

class Charge(object):

    def __init__(self,x0,y0,q):
        self.x0 = x0
        self.y0 = y0
        self.q = q

class Vector(object):

    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __str__(self):
        return "norm:{0}, x={1},y={2}\n".format(self.norm(),self.x, self.y)

    def norm(self):
        return np.sqrt(self.x**2+self.y**2)

class Field(object):
    """
        The main field object, E and B are derived from this

        Contains the meshgrid and plot functions
    """

    def __init__(self):
        # Make the grid
        self.X, self.Y = np.meshgrid(np.arange(-16,16,0.5),np.arange(-16,16,0.5))
        self.i=self.X.shape[0]
        self.j=self.X.shape[1]
        self.Vx = np.zeros([self.i,self.j])
        self.Vy = np.zeros([self.i,self.j])
        self.charges =[]

    def totalCharge(self):
        sum=0
        for i in self.charges:
            sum = sum+np.abs(i.q)
        return sum

    def clear(self):
        self.Vx = np.zeros([self.i,self.j])
        self.Vy = np.zeros([self.i,self.j])
        self.charges=[]

    def field(self, x0, y0, I):
        r = np.sqrt((self.X-x0)**2+(self.Y-y0)**2)
        eps=0.0001
        reciproke = 1.0/(r+eps)/2/np.pi
        Bx_ = self.u0*I * reciproke**2 * (self.Y-y0)
        By_ = self.u0*I * reciproke**2 * -(self.X-x0)
        return Bx_,By_

    def add(self,x0, y0, charge):
        VxTemp,  VyTemp = self.field(x0,y0, charge)
        self.Vx = self.Vx + VxTemp
        self.Vy = self.Vy + VyTemp
        mycharge = Charge(x0,y0,charge)
        self.charges.append(mycharge)

    def fieldAtpoint(self, xCharge, yCharge, q, x, y):
        return 0,0

    def probe(self,x0, y0):
        Fx=0
        Fy=0
        for c in self.charges:
            Fxt,Fyt=self.fieldAtpoint(c.x0,c.y0,c.q,x0,y0)
            Fx = Fx + Fxt
            Fy = Fy + Fyt
        return Vector(Fx, Fy)

    def plot(self, type="vector"):
        """
            plot(<type>)

            plot("vector"), plot("line"), plot("vetor and line")
        """
        #norm = np.sqrt(self.Vx**2+self.Vy**2)
        norm=0.5
        self.Vxp = self.Vx/norm
        self.Vyp = self.Vy/norm
        plt.figure(figsize=(20,10))
        res = 2

        if "vector" in type:
            plt.quiver(
                        self.X[::res,::res],self.Y[::res,::res],
                        self.Vxp[::res,::res],self.Vyp[::res,::res],
                        pivot="mid",scale=self.scalefactor,width=0.002)
        if "line" in type:
            plt.streamplot(self.X,self.Y,self.Vxp,self.Vyp)

        for c in self.charges:
            if c.q>0:
                plt.plot(c.x0,c.y0,'ro',markersize=15)
            if c.q<0:
                plt.plot(c.x0,c.y0,'go',markersize=15)

    def save(self, name):
        plt.savefig(name)

    def show(self):
        plt.show()

class BField(Field):
    """
        Calculate the Magnetic Field using wire elements.

        .. math::

           B=\\frac{\\mu_0 \cdot I}{2\\pi r}

        We calculate :math:`\\vec{B}` as being perpendicular to :math:`\\vec{r}`


    """
    u0 = 4.0 * np.pi * 10**-7
    scalefactor=.0000012
    def field(self, x0, y0, I):
        r = np.sqrt((self.X-x0)**2+(self.Y-y0)**2)
        eps=0.0001
        reciproke = 1.0/(r+eps)/2/np.pi
        Bx_ = self.u0*I * reciproke**2 * (self.Y-y0)
        By_ = self.u0*I * reciproke**2 * -(self.X-x0)
        return Bx_,By_

class EField(Field):
    """
        Calculate the Electric Field using point charges.

        .. math::


           E=\\frac{1}{4\\pi \\varepsilon_0} \\frac{\\left|q\\right|}{r^2}

        We calculate :math:`\\vec{E}` as being parallel to :math:`\\vec{r}`

        Some examples:
        ~~~~~~~~~~~~~~

        >>> import em
        >>> E = em.EField()
        >>> E.add(0,0,3e-9)
        >>> E.plot()
        >>> E.save('./pics/onecharge.pdf')

        .. image:: ../pics/onecharge.pdf
           :height: 100px

        >>> import em
        >>> E = em.EField()
        >>> E.add(5,0,3e-9)
        >>> E.add(-5,0,-3e-9)
        >>> E.plot("line")
        >>> E.save('./pics/twocharge.pdf')

        .. image:: ../pics/twocharge.pdf
           :height: 100px


    """

    e0 = 8e-12
    scalefactor=1500
    oneoverfourpiepsilonnaught=9.0e9

    def fieldAtpoint(self, cx,cy,q,x,y):
        r = np.sqrt((x-cx)**2+(y-cy)**2)
        eps=0.0001
        reciproke = 1.0/(r+eps)**2*self.oneoverfourpiepsilonnaught
        Ex_ = q * reciproke * (x-cx)
        Ey_ = q * reciproke * (y-cy)
        return Ex_,Ey_

    def field(self, x0, y0, q):
        r = np.sqrt((self.X-x0)**2+(self.Y-y0)**2)
        eps=0.0001
        reciproke = 1.0/(r+eps)**2*self.oneoverfourpiepsilonnaught
        Ex_ = q * reciproke * (self.X-x0)
        Ey_ = q * reciproke * (self.Y-y0)
        return Ex_,Ey_

if __name__ == "__main__":
    mfield = BField()

    mfield.add(0,0,10)
    mfield.plot("vector and line")
    mfield.show()

    efield = EField()
    efield.add(3,0,1e-9)
    efield.add(-3,0,-1e-9)
    print (efield.probe(1,1))
    efield.plot("vector and line")
    efield.show()
