import parse from "html-react-parser";

export function textParse(string, language) {
  // replace new line chars with spaces unless there are 2 consecutively
  for (let i = 0; i < string.length; i++) {
    if (string.substring(i, i + 1) === "\n") {
      if (string.substring(i + 1, i + 2) !== "\n") {
        string = string.substring(0, i) + " " + string.substring(i + 1);
      } else i++;
    }
  }

  // if HTML, replace <ansired> with proper HTML tag
  if (language === "HTML") {
    while (string.indexOf("<ansired>") !== -1) {
      const index = string.indexOf("<ansired>");
      string =
        string.substring(0, index) +
        '<font color="red">' +
        string.substring(index + 9);
    }

    while (string.indexOf("</ansired>") !== -1) {
      const index = string.indexOf("</ansired>");
      string =
        string.substring(0, index) + "</font>" + string.substring(index + 10);
    }
  }

  // delete ansired tag
  else {
    while (string.indexOf("<ansired>") !== -1) {
      const index = string.indexOf("<ansired>");
      string = string.substring(0, index) + string.substring(index + 9);
    }

    while (string.indexOf("</ansired>") !== -1) {
      const index = string.indexOf("</ansired>");
      string = string.substring(0, index) + string.substring(index + 10);
    }
  }

  return parse(string);
}

export function isValidParameter(value, param_type) {
  // make null inputs valid to avoid handling as an error
  if (value === "") return true;

  if (param_type === "integer") {
    value = Number(value);
    return Number.isInteger(value);
  } else if (param_type === "positive integer") {
    value = Number(value);
    return value > 0 && Number.isInteger(value);
  } else if (param_type === "even positive integer") {
    value = Number(value);
    return value > 0 && Number.isInteger(value) && value % 2 === 0;
  } else if (param_type === "non-negative integer") {
    value = Number(value);
    return value >= 0 && Number.isInteger(value);
  } else if (param_type === "float") {
    value = Number(value);
    return !(value % 1 === 0);
  } else if (param_type === "positive float") {
    value = Number(value);
    return !(value % 1 === 0) && value > 0;
  } else if (param_type === "non-negative float") {
    value = Number(value);
    return !(value % 1 === 0) && value >= 0;
  } else if (param_type === "probability") {
    value = Number(value);
    return !(value % 1 === 0) && value >= 0 && value <= 1;
  } else if (param_type === "comma-separated list") {
    // return ','.join(v.strip() for v in value.split(','))
    // what makes a string not a good list?
    return typeof value == "string" && value.indexOf(",") > 0;
  } else if (param_type === "string") {
    return typeof value === "string" || value instanceof String;
  } else {
  /*
  else if param_type == "function":
      return value.strip() # TODO maybe do something more sophisticated for functions?
  
  */
    //throw new CustomException('FAVITES-Lite bug: Invalid parameter type: %s' % param_type);
    //console.log("FAVITES-Lite bug: Invalid parameter type: %s" % param_type);
    //throw new ReferenceError('FAVITES-Lite bug: Invalid parameter type: %s' % param_type);
  }

  return false;
}

export const status = {
  NOT_SELECTED: 0,
  INCOMPLETE: 1,
  COMPLETE: 2,
  ERROR: 3
}