import './App.css';
import InitPage from './InitPage/InitPage';
import ItemDetailPage from './ItemDetailPage/ItemDetailPage';
import IngredientDetailPage from './ItemDetailPage/IngredientDetailPage';
import CreateCustomPage from './CreateCustomPage/CreateCustomPage';
import EditCustomPage from './EditCustomPage/EditCustomPage';
import MyPage from './MyPage/MyPage';
import Test from './Test'
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import React from 'react';
import ListPage from "./ListPage/ListPage";

function App() {

  return (
    <div className="App">
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<InitPage />} />
          <Route path="/:type" element={<ListPage />} />
          <Route path="/custom/:id/edit" element={<EditCustomPage />} />
          <Route path='/custom/create' element={<CreateCustomPage />} />
          <Route path="/ingredient/:id" element={<IngredientDetailPage />} />
          <Route path="/:type/:id" element={<ItemDetailPage />} />
          <Route path="/mypage" element={<MyPage />} />
          <Route path="/test" element={<Test />} />
        </Routes>
      </BrowserRouter >
    </div >
  );
}

export default App;