import styles from "./Component.module.css";

const Component = (props) => {
  const { name, onClick } = props;

  return (
    <div className={styles.Main} onClick={onClick}>
      <h4>{name}</h4>
      <span>Not Selected</span>
    </div>
  );
};

export default Component;
