import sys
from django.http import HttpResponse
import matplotlib as mpl
mpl.use('Agg') # Required to redirect locally
import matplotlib.pyplot as plt
import numpy as np
from numpy.random import rand
try:
    # Python 2
    import cStringIO
except ImportError:
    # Python 3
    import io

def get_image(request):
   """
   This is an example script from the Matplotlib website, just to show
   a working sample >>>
   """
   N = 50
   x = np.random.rand(N)
   y = np.random.rand(N)
   colors = np.random.rand(N)
   area = np.pi * (15 * np.random.rand(N))**2 # 0 to 15 point radiuses
   plt.scatter(x, y, s=area, c=colors, alpha=0.5)
   """
   Now the redirect into the cStringIO or BytesIO object >>>
   """
   if cStringIO in sys.modules:
      f = cStringIO.StringIO()   # Python 2
   else:
      f = io.BytesIO()           # Python 3
   plt.savefig(f, format="png", facecolor=(0.95,0.95,0.95))
   plt.clf()
   """
   Add the contents of the StringIO or BytesIO object to the response, matching the
   mime type with the plot format (in this case, PNG) and return >>>
   """
   return HttpResponse(f.getvalue(), content_type="image/png")