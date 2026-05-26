import React, { useState, useEffect } from 'react';
import { Layout, Menu, Breadcrumb } from 'antd';
import {
  DashboardOutlined,
  StockOutlined,
  LineChartOutlined,
  FundOutlined,
  HistoryOutlined,
  SettingOutlined,
} from '@ant-design/icons';
import './App.css';
import Dashboard from './pages/Dashboard';
import Strategies from './pages/Strategies';
import Backtests from './pages/Backtests';
import Holdings from './pages/Holdings';
import Trades from './pages/Trades';
import Settings from './pages/Settings';

const { Header, Content, Footer, Sider } = Layout;

function App() {
  const [collapsed, setCollapsed] = useState(false);
  const [currentPage, setCurrentPage] = useState('dashboard');

  const renderContent = () => {
    switch (currentPage) {
      case 'dashboard':
        return <Dashboard />;
      case 'strategies':
        return <Strategies />;
      case 'backtests':
        return <Backtests />;
      case 'holdings':
        return <Holdings />;
      case 'trades':
        return <Trades />;
      case 'settings':
        return <Settings />;
      default:
        return <Dashboard />;
    }
  };

  return (
    <Layout style={{ minHeight: '100vh' }}>
      <Sider theme="light" collapsible collapsed={collapsed} onCollapse={setCollapsed}>
        <div className="logo">
          <h2 style={{ padding: '16px', margin: 0, textAlign: 'center' }}>
            📊 Quant
          </h2>
        </div>
        <Menu
          theme="light"
          mode="inline"
          selectedKeys={[currentPage]}
          onClick={(e) => setCurrentPage(e.key)}
          items={[
            {
              key: 'dashboard',
              icon: <DashboardOutlined />,
              label: '仪表盘',
            },
            {
              key: 'strategies',
              icon: <FundOutlined />,
              label: '策略管理',
            },
            {
              key: 'backtests',
              icon: <LineChartOutlined />,
              label: '回测分析',
            },
            {
              key: 'holdings',
              icon: <StockOutlined />,
              label: '持仓管理',
            },
            {
              key: 'trades',
              icon: <HistoryOutlined />,
              label: '交易记录',
            },
            {
              key: 'settings',
              icon: <SettingOutlined />,
              label: '系统设置',
            },
          ]}
        />
      </Sider>
      <Layout>
        <Header
          style={{
            background: '#fff',
            padding: '0 24px',
            boxShadow: '0 2px 8px rgba(0,0,0,0.1)',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'space-between',
          }}
        >
          <h1 style={{ margin: 0 }}>量化交易平台</h1>
          <div>用户: admin</div>
        </Header>
        <Content style={{ margin: '24px 16px' }}>
          <Breadcrumb style={{ margin: '16px 0' }}>
            <Breadcrumb.Item>首页</Breadcrumb.Item>
            <Breadcrumb.Item>{currentPage}</Breadcrumb.Item>
          </Breadcrumb>
          <div
            style={{
              padding: 24,
              background: '#fff',
              borderRadius: '4px',
            }}
          >
            {renderContent()}
          </div>
        </Content>
        <Footer style={{ textAlign: 'center' }}>
          Quant Trading Platform ©2026 - All Rights Reserved
        </Footer>
      </Layout>
    </Layout>
  );
}

export default App;
