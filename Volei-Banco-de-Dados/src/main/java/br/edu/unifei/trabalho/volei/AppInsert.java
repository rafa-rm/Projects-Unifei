//Rafael Rocha Maciel - 2018005619
//Laboratório de Banco de Dados - ECOT13
//Universidade Federal de Itajub�

package br.edu.unifei.trabalho.volei;

import java.awt.Color;

import javax.persistence.EntityManager;
import javax.persistence.EntityManagerFactory;
import javax.persistence.Persistence;

public class AppInsert {

	public static void main(String[] args) {
		
        EntityManagerFactory emf = Persistence.createEntityManagerFactory("voleiPU");
        EntityManager em = emf.createEntityManager();
        em.getTransaction().begin();
			
		//Criando um jogador
		Jogador j1 = new Jogador();
		j1.setAltura(195);
		j1.setIdade(25);
		j1.setNome("Giba");
		j1.setNumeroCamisa(7);
		j1.setPeso(75.5f);
		j1.setTempoProfissional(7);
		j1.setPosicao(PosicaoEnum.PONTEIRO);


		//Criando um posicionamento na rede  
	    Rede jogadorRede = new Rede();
	    jogadorRede.setPosicaoRotacao(RotacaoEnum.CENTRO);
	    j1.setPosicionamento(jogadorRede);
		em.persist(j1);
	    em.persist(jogadorRede);
	    
		//Criando um posicionamento no fundo
	    FundoQuadra jogadorFundo = new FundoQuadra();
	    jogadorFundo.setPosicaoRotacao(RotacaoEnum.ESQUERDA);
	    em.persist(jogadorFundo);
	    
	    //Criar equipe, treinador e torcida
	    //Equipe
	    Equipe e1 = new Equipe();
	    e1.setCorCamisa(Color.YELLOW);
	    e1.setLado(LadoEnum.CASA);
	    e1.setLocalidade("Am�rica do sul");
	    e1.setNome("Brasil");
	    e1.getJogadores().add(j1);
	    
	    //Treinador
	    Treinador t1 = new Treinador();
	    t1.setNome("Bernardinho");
	    t1.setEquipe(e1);
	    t1.setExJogador(true);
	    t1.setTempoProfissao(30);
	    em.persist(t1);
	    
	    //Torcida
	    Torcida torcida1 = new Torcida();
	    torcida1.setNome("Brasileiros");
	    torcida1.setAnimacao(10.0f);
	    torcida1.setEquipe(e1);
	    torcida1.setQuantidade(10000);
	    torcida1.setGrito("Vai Brasil!!!");
	    em.persist(torcida1);
	    
	    //Setando treinador e torcida na equipe
	    e1.setTreinador(t1);
	    e1.setTorcida(torcida1);
	    em.persist(e1);
  	    
  	    
  	    //Criando o SetDisputado 1
  	    SetDisputado s1 = new SetDisputado();
  	    s1.setDuracaoMinutos(40);
  	    s1.setVencedor(e1);
  	    em.persist(s1);
  	    
  	    //Criando a jogada 1
  	    Jogada jogada1 = new Jogada();
  	    jogada1.setFundamento(FundamentoEnum.BLOQUEIO);
  	    jogada1.setJogador(j1);
  	    jogada1.setTempo(2);
  	    em.persist(jogada1);
  	    
  	    //Criando 2 jogadas
  	    Jogada jogada2 = new Jogada();
  	    Jogada jogada3 = new Jogada();
  	    jogada3.setJogador(j1);
  	    em.persist(jogada2);
  	    em.persist(jogada3);
  	    
  	    //Criando o set 2 e 3
  	    SetDisputado s2 = new SetDisputado();
  	    s2.setDuracaoMinutos(20);
  	    s2.setVencedor(e1);
  	    em.persist(s2);
  	    
  	    SetDisputado s3 = new SetDisputado();
  	    s3.setDuracaoMinutos(30);
  	    s3.setVencedor(e1);
  	    em.persist(s3);
  	        
  	    //Criando 1 ponto
  	    Ponto p1 = new Ponto();
  	    p1.setDuracaoSegundos(30);
  	    p1.getJogadas().add(jogada1);
  	    p1.getJogadas().add(jogada2);
  	    p1.getJogadas().add(jogada3);
  	    p1.setSet(s1);
  	    p1.setEquipe(e1);   
  	    em.persist(p1);
  	    
  	    
  	    
  	    //Criando a equipe 2
  	    Equipe e2 = new Equipe();
  	    e2.setNome("Argentina");
  	    Ponto p2 = new Ponto();
  	    e2.getPontos().add(p2);
  	    p2.setEquipe(e2);
  	    em.persist(e2);
  	    em.persist(p2);
	    
	    //Criando o est�dio
	    Estadio es1 = new Estadio();
	    es1.setNome("Maracanãzinho");
	    es1.setCapacidadeMaxima(20000);
	    es1.setTorcida1(torcida1);
	    em.persist(es1);
	    
	    //Criando partida 1
	    Partida part1 = new Partida();
	    part1.setEquipe1(e1);
	    part1.setEquipe1(e2);
	    part1.setEstadio(es1);
	    part1.setLocalidade("Rio de Janeiro");
	    part1.setPublico(12000);
	    part1.setVencedor(e1);
	    part1.getSets().add(s1);
	    part1.getSets().add(s2);
	    part1.getSets().add(s3);
	    em.persist(part1);
	    
	    //Criando partida 2 e 3
	    Partida part2 = new Partida();
	    Partida part3 = new Partida();
	    em.persist(part2);
	    em.persist(part3);

	    //Criando o torneio
	    Torneio tor1 = new Torneio();
	    tor1.setNome("Mundial 2022");
	    tor1.setGanhador(e1);
	    tor1.setPremiacao(65000.00f);
	    tor1.setOrganizador("FIVB");
	    tor1.getPartidas().add(part1);
	    tor1.getPartidas().add(part2);
	    tor1.getPartidas().add(part3);
	    em.persist(tor1);

	    //Criando Regras
	    Regra r1 = new Regra();
	    r1.setDescricao("Encostar na rede");
	    r1.setAcaoTomada("Ponto para o outro time");
	    Regra r2 = new Regra();
	    r2.setDescricao("Pisar na linha de 3");
	    em.persist(r1);
	    em.persist(r2);
	    
	    //Criando Arbitro
	    Arbitro a1 = new Arbitro();
	    a1.setNome("José da Silva");
	    a1.setPonto(p1);
	    a1.getRegras().add(r1);
	    a1.getRegras().add(r2);
	    a1.setPartida(part1);
	    a1.setDecisaoPonto(LadoEnum.CASA);
	    a1.setPontuacaoEquipe1(18);
	    a1.setPontuacaoEquipe2(22);
	    em.persist(a1);
	    
        em.getTransaction().commit();
        em.close();
        emf.close();
	}
}
