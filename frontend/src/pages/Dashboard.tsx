import React from 'react';
import { Row, Col, Card, Statistic, Table, Button } from 'antd';
import { ArrowUpOutlined, ArrowDownOutlined } from '@ant-design/icons';

const Dashboard: React.FC = () => {
  const columns = [
    {
      title: '策略名称',
      dataIndex: 'name',
      key: 'name',
    },
    {
      title: '状态',
      dataIndex: 'status',
      key: 'status',
    },
    {
      title: '收益率',
      dataIndex: 'return',
      key: 'return',
    },
    {
      title: '操作',
      key: 'action',
      render: () => (
        <>
          <Button type="link">查看</Button>
          <Button type="link" danger>
            删除
          </Button>
        </>
      ),
    },
  ];

  const data = [
    {
      key: '1',
      name: '均线突破策略',
      status: '运行中',
      return: '+15.3%',
    },
    {
      key: '2',
      name: 'RSI策略',
      status: '已停止',
      return: '-2.1%',
    },
  ];

  return (
    <div>
      <Row gutter={16} style={{ marginBottom: '24px' }}>
        <Col xs={24} sm={12} lg={6}>
          <Card>
            <Statistic
              title="总资产"
              value={100000}
              prefix="¥"
              valueStyle={{ color: '#1890ff' }}
            />
          </Card>
        </Col>
        <Col xs={24} sm={12} lg={6}>
          <Card>
            <Statistic
              title="可用资金"
              value={50000}
              prefix="¥"
              valueStyle={{ color: '#52c41a' }}
            />
          </Card>
        </Col>
        <Col xs={24} sm={12} lg={6}>
          <Card>
            <Statistic
              title="浮动盈亏"
              value={5300}
              prefix="¥"
              valueStyle={{ color: '#52c41a' }}
              prefix={<ArrowUpOutlined />}
            />
          </Card>
        </Col>
        <Col xs={24} sm={12} lg={6}>
          <Card>
            <Statistic
              title="收益率"
              value={5.3}
              suffix="%"
              valueStyle={{ color: '#52c41a' }}
              prefix={<ArrowUpOutlined />}
            />
          </Card>
        </Col>
      </Row>

      <Row gutter={16}>
        <Col xs={24} lg={12}>
          <Card title="策略运行情况" loading={false}>
            <Table columns={columns} dataSource={data} pagination={false} />
          </Card>
        </Col>
        <Col xs={24} lg={12}>
          <Card title="关键指标" loading={false}>
            <div style={{ padding: '24px' }}>
              <Row gutter={16}>
                <Col xs={12}>
                  <div style={{ textAlign: 'center' }}>
                    <div style={{ fontSize: '12px', color: '#666' }}>Sharp比率</div>
                    <div style={{ fontSize: '20px', fontWeight: 'bold' }}>1.45</div>
                  </div>
                </Col>
                <Col xs={12}>
                  <div style={{ textAlign: 'center' }}>
                    <div style={{ fontSize: '12px', color: '#666' }}>最大回撤</div>
                    <div style={{ fontSize: '20px', fontWeight: 'bold' }}>-8.3%</div>
                  </div>
                </Col>
              </Row>
              <Row gutter={16} style={{ marginTop: '16px' }}>
                <Col xs={12}>
                  <div style={{ textAlign: 'center' }}>
                    <div style={{ fontSize: '12px', color: '#666' }}>胜率</div>
                    <div style={{ fontSize: '20px', fontWeight: 'bold' }}>62.5%</div>
                  </div>
                </Col>
                <Col xs={12}>
                  <div style={{ textAlign: 'center' }}>
                    <div style={{ fontSize: '12px', color: '#666' }}>总交易数</div>
                    <div style={{ fontSize: '20px', fontWeight: 'bold' }}>48</div>
                  </div>
                </Col>
              </Row>
            </div>
          </Card>
        </Col>
      </Row>
    </div>
  );
};

export default Dashboard;
