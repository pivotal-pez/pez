# Haas inception

## Goals
- a starting point for all things pez
- automated provisioning of servers, storage, etc
- provision from bare metal
- network config automation
- easily supported provisioning
- leasing or calendaring (inventory management)
- self service (no human interaction)
- ability to yield back resources on schedule or on-demand
- archive leased compute
- cli/non-gui method of interacting with pez
- exec dash (w/ utilization mapped to cost center)
- showback / billback
- easy point and click UX
- deliver by EOY 2015
- Inventory Availability View (who has what? what can i grab?)
- quotas for users
- status health page (working or not? custom messaging to users)
- easy on boarding of compute resources into HaaS Pool
- Multi-DC support at inventory level
- Dog Food
- Vend PXI booted servers
- Vend VShpere
- Vend PCF
- lessen AWS spend
- heterogenius infrastructure
- garbage collection / tenant management

## Risk
- 1 User Experience
  __mitigation__
    - user stories with clear design goals
    - user interviews
    - ux design resources from labs
    - prioritize webui as main client over a cli client

- 2 Dedicated Resources
  __mitigation__
    - easy dev onboarding
    - automations for everything
    - logging/metrics
    - open backlog for community contribs
    - feature voting from pez community
    - PTO calendars shared

- 3 Scope Creep
  __mitigation__
    - feature voting
    - user interviews
    - keep to our methodology (Agile)
    - lean on Joe S. for Project organization
    - direct contact with PO (patrick n, sean m)

- 4a Capacity
  __mitigation__
    - allow transparency into capacity and a users place in line
    - define capacity limits
    - define offering sizes

- 4b Boilerplate work
  __mitigation__
    - early spikes to vet viability of existing solutions 
    - clear outcomes from stories and spikes

- 5a Multi-DC
  __mitigation__
    - properly prioritize our work

- 5b Cost/Funding
  __mitigation__
    - Dont Fail :)
    - make this a shining example of what/why Pivotal should invest
    - Ford should meet w/ people and pitch it as only he can

## Roles / Personas
- Capacity Admin
- Network Admin
- Storage Admin
- Exec / Overlord
- Consumers
  - Metal
  - VShpere
  - PCF
  - OpenStack
  - Data
- Consumer Admin

## Activities
- Capacity Admin should be able to onboard servers
- Capactiy Admin should be able to offboard consumers
- Capacity Admin should be able to manage servers
- Network Admin should be able to configur vlan
- Network Admin should be able to provision vlan
- Network Admin should be able to configure router
- Network Admin should be able to configure ip subnet
- Network Admin should be able to configure switches
- Network Admin should be able to configure storage network routing
- Storage Admin should be able to create datastores
- Exec/Overlord should be able to check consumed resources
- Exec/Overlord should be able to prioritize consumtion of resources
- Exec/Overlord should be able to check showback / billback
- Consumer should be able to see what is available
- Consumer should be able to request an available resource
- Consumer should be able to check what is currently issued to them (detail & list)
- Consumer should be able to extend the lease of what they have
- Consumer should be able to return what they have
- Consumer should be notified when their resource expires
- Consumer Admin should be able to extend a consumer's lease
- Consumer Admin should be able to manage inventory
- Consumer Admin should be able to define inventory

## Retro
- Positives
  - holistic view of project
  - defined scope
  - real pez dev effort has begun
  - inn keeper exists
  - we have a mvp | backlog items | established mvp
  - got through agenda
  - end goal looks good
  - lots of work to do

- Negatives
  - pez ops not all present for inception | more input from pez team
  - stay on track during inception
  - food situation during lunch

- Questions or What still puzzles us
  - what comes after mvp
  - input from data team?
  - is this inline with expectations for inception
  - how long before we actually code
  - mvp too basic

