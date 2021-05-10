import {ReactElement} from "react";
import {Divider} from "antd";
import Uploader from "../components/Uploader";
import Handler from "../components/Handler";
import styled from "styled-components";

const HomeViewWrapper = styled.div`
  height: 100vh;
  width: 100vw;

  display: flex;
  align-items: center;
`;

const ScreenPart = styled.div`
  flex: 1;

  display: flex;
  align-items: center;
  justify-content: center;
`;

const VerticalDivider = styled(Divider)`
  height: 95%;
`;

function HomeView(): ReactElement {
  return (
    <HomeViewWrapper>
      <ScreenPart>
        <Uploader/>
      </ScreenPart>
      <VerticalDivider type="vertical"/>
      <ScreenPart>
        <Handler/>
      </ScreenPart>
    </HomeViewWrapper>
  );
}

export default HomeView;
