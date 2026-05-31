export function AccountManagementPage() {
  return (
    <div className="page-stack">
      <h2>계좌관리</h2>
      <p className="lead">브로커 계좌 연결 상태, 계좌별 설정, 사용 여부를 관리합니다.</p>

      <section className="panel">
        <h3>등록 계좌</h3>
        <table className="basic-table" aria-label="등록 계좌 목록">
          <thead>
            <tr>
              <th>브로커</th>
              <th>계좌번호</th>
              <th>계좌명</th>
              <th>연결상태</th>
              <th>기본계좌</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>한국투자증권</td>
              <td>12345678-01</td>
              <td>주식 메인</td>
              <td className="ok">연결됨</td>
              <td>Y</td>
            </tr>
            <tr>
              <td>키움증권</td>
              <td>98765432-01</td>
              <td>모의투자</td>
              <td className="err">점검 필요</td>
              <td>N</td>
            </tr>
          </tbody>
        </table>
      </section>
    </div>
  );
}
