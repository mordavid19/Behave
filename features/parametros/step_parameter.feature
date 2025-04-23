Feature: Horario

Scenario: Verify Day and Night Schedule
Given I reach office at "day" shift 
And I reach office at "night" shift 


Scenario: Verify Day and Night Schedule
Given llego a la oficina en el turno "day"
And llego a la oficina en el turno "night"

Scenario: Force failure
Given I reach office at "tarde" shift
And I reach office at "night" shift
