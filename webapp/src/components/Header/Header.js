import styles from "./Header.module.css";

const Header = (props) => {
  const { className } = props;

  return (
    <div className={className}>
      <h1>FAVITES-Lite <span>Config Designer</span></h1>
    </div>
  );
};

export default Header;
