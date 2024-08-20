from une_ai.models import Agent, GridMap

class ConnectFourPlayer(Agent):

    def __init__(self, agent_name, agent_program):
        super().__init__(agent_name, agent_program)
        if 'game-board-sensor' not in self._sensors:
            self.add_all_sensors()
        if 'checker-handler' not in self._actuators:
            self.add_all_actuators()
        self.add_all_actions()

    # TODO
    # add all the necessary sensors as per the requirements
    def add_all_sensors(self):
        self.add_sensor('game-board-sensor', GridMap(7, 6), self.validate_gridmap)  # Correct dimensions
        self.add_sensor('powerups-sensor', {'Y': None, 'R': None}, self.validate_powerups)
        self.add_sensor('turn-taking-indicator', 'Y', self.validate_turn_indicator)

    # TODO
    # add all the necessary actuators as per the requirements
    def add_all_actuators(self):
        self.add_actuator('checker-handler', ('release', 0), self.validate_checker_handler)
        self.add_actuator('powerup-selector', False, self.validate_powerup_selector)

    # TODO
    # add all the necessary actions as per the requirements
    def add_all_actions(self):
        for i in range(7):
            if f'release-{i}' not in self._actions:
                self.add_action(f'release-{i}', lambda i=i: self.actuate_checker('release', i))
            if f'popup-{i}' not in self._actions:
                self.add_action(f'popup-{i}', lambda i=i: self.actuate_checker('popup', i))
            if f'use-power-up-{i}' not in self._actions:
                self.add_action(f'use-power-up-{i}', lambda i=i: self.use_power_up(i))

    def actuate_checker(self, action_type, column):
        self.set_actuator_value('checker-handler', (action_type, column))
        return {'checker-handler': (action_type, column)}

    def use_power_up(self, column):
        self.set_actuator_value('powerup-selector', True)
        self.set_actuator_value('checker-handler', ('release', column))
        return {'powerup-selector': True, 'checker-handler': ('release', column)}

    def set_actuator_value(self, actuator_name, value):
        if actuator_name in self._actuators:
            validation_function = self._actuators[actuator_name]['validation-function']
            assert validation_function(value), f"The value {value} is not a valid value for the actuator '{actuator_name}'"
            self._actuators[actuator_name]['value'] = value
        else:
            raise AttributeError(f"Actuator '{actuator_name}' not found")

    def validate_gridmap(value):
        try:
            if isinstance(value, GridMap):
                if value.get_width() == 7 and value.get_height() == 6:
                    return True
        except Exception as e:
            print(f"Validation failed: {e}")
        return False

    def validate_powerups(value):
        if isinstance(value, dict) and 'Y' in value and 'R' in value:
            return True
        return False

    def validate_turn_indicator(value):
        if value in ['Y', 'R']:
            return True
        return False

    def validate_checker_handler(value):
        if isinstance(value, tuple) and len(value) == 2:
            action_type, column = value
            if action_type in ['release', 'popup'] and 0 <= column <= 6:
                return True
        return False

    def validate_powerup_selector(value):
        return isinstance(value, bool)
