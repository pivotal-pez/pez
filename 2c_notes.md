# 2c Buildout

## vcd lease responsibilities
  * policies
    * vcd 7 days delete storage ( this is not a dispenser responsibility )
    * vcd runtime lease never expires (this is the responsibility of dispenser)

## deployment
  * is there running pod on slot & lease expired?
    * if yes, destroy

  * safety check before deploying new pod (there should not be anything running)

tasks -> task block in xml response href poll from status, when creating the vapp from the template

## timeout
  * 20 min max then fail hard

## investigate power down vapp

## remap pcfaas-slotX.pez.pivotal.io
  * using pcfaas-username.pez.pivotal.io

  teardown removes the dns record
  ?? how do we solve the gorouter domain remap?
  maybe url re-writes in front of haproxy

  maybe a pool of IPs that we bind the slots to at random,
  so the slot DNS records
