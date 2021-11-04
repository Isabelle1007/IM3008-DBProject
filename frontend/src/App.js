import SearchPage from './components/search_page'
import Header from './components/header'
import './App.css';
import DualSlider from "./components/dual_range_slider"

function App() {
  return (
    <div className="App">
      <Header />
      <SearchPage/>
      {/* <DualSlider/> */}
    </div>
  );
}

export default App;
