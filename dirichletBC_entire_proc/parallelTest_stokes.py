
# coding: utf-8

# In[1]:


import underworld as uw
import glucifer


# In[2]:


q1_mesh = uw.mesh.FeMesh_Cartesian( elementRes=(4,10))

vField = uw.mesh.MeshVariable(q1_mesh,nodeDofCount=2)
pField = uw.mesh.MeshVariable(q1_mesh.subMesh,nodeDofCount=1)
top = q1_mesh.specialSets["MaxJ_VertexSet"]
base = q1_mesh.specialSets["MinJ_VertexSet"]


# In[3]:


mySet = q1_mesh.specialSets["Empty"]


# In[4]:


for ind, pos in enumerate(q1_mesh.data):
    if pos[1] < 0.6:
        mySet.add(ind)


# In[5]:


vField.data[top.data] = [-1.0, 0.]
vField.data[mySet.data] = [1.0, 0.]


# In[6]:


vBCs = uw.conditions.DirichletCondition(vField,indexSetsPerDof=(mySet+top,top+base))


# In[7]:


store = glucifer.Store('model')


# In[8]:


fig = glucifer.Figure( store )


# In[9]:


fig.append( glucifer.objects.VectorArrows(q1_mesh, vField) )
# fig.append( glucifer.objects.Mesh(q1_mesh, nodeNumbers=True))


# In[10]:


fig.show()


# In[11]:


stokes = uw.systems.Stokes(vField, pField, 
                           fn_viscosity=1.,
#                            conditions=vBCs)
                           conditions=vBCs, _removeBCs=False)
solver = uw.systems.Solver(stokes)
# solver.set_inner_method("nomg")


# In[12]:


solver.solve()
store.step += 1


# In[13]:


fig.show()


# In[ ]:




