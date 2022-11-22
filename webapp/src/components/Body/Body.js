import { useSelector, useDispatch } from "react-redux";
import { set } from "../../features/config/configSlice";
import styles from "./Body.module.css";

const Body = (props) => {
  const { className } = props;
  const config = useSelector((state) => state.config.value);
  const dispatch = useDispatch();

  return (
    <div className={className}>
      {JSON.stringify(config)}
      <br />
      <button onClick={() => dispatch(set({test: "test"}))}>Test 1</button>
      <button onClick={() => dispatch(set({}))}>Test 2</button>
      <button onClick={() => dispatch(set({test: "test", test2: {test: "test"}}))}>Test 3</button>
    </div>
  );
};

export default Body;
