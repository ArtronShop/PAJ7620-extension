Blockly.Python['paj7620_is_gesture'] = function (block) {
  Blockly.Python.definitions_['import_PAJ7620'] = 'import PAJ7620';

  var dropdown_gesture = block.getFieldValue('gesture');

  var code = `PAJ7620.isGesture(${dropdown_gesture})`;
  return [code, Blockly.Python.ORDER_NONE];
};
