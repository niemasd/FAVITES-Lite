import { useSelector, useDispatch } from "react-redux";
import { Typography } from "@mui/material";
import {
  ModelCitation,
  ModelDescription,
  ModelParameters,
  ModelProperties,
  ModelRequirements,
  ModelSelect,
  ParametersSelect,
} from "./BodyModules";
import styles from "./Body.module.css";
import globalJSON from "../../files/global.json";

const Body = (props) => {
  const { className } = props;
  const config = useSelector((state) => state.config.value);
  const selected = useSelector((state) => state.selected.value);

  return (
    <div className={`${className} ${styles.Main}`}>
      {selected && (
        <>
          <Typography variant="h3">{selected}</Typography>
          <br />
          <Typography>{globalJSON.DESC[selected]}</Typography>
          <br />
          <Typography variant="h4">Step 1: Choose Model</Typography>

          <ModelSelect />
        </>
      )}

      {config[selected] && config[selected]["model"] && (
        <>
          <ModelDescription />
          <ModelCitation />
          <ModelProperties />
          <ModelRequirements />

          <Typography variant="h4">Step 2: Choose Parameters</Typography>
          <br />
          {/* <ModelParameters /> */}
          <ParametersSelect />
        </>
      )}
    </div>
  );
};

export default Body;
