package br.edu.unifei.trabalho.volei.swing;

import java.awt.EventQueue;

import javax.persistence.EntityManager;
import javax.persistence.EntityManagerFactory;
import javax.persistence.Persistence;
import javax.swing.DefaultListModel;
import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;

import br.edu.unifei.trabalho.volei.Jogador;
import br.edu.unifei.trabalho.volei.PosicaoEnum;

import javax.swing.JTextField;
import javax.swing.JLabel;
import java.awt.Font;
import javax.swing.JSpinner;
import javax.swing.JList;
import javax.swing.JOptionPane;
import javax.swing.ListSelectionModel;
import javax.swing.JButton;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;


public class JogadorFormAlterar extends JFrame {

	private static final long serialVersionUID = -1393725916291997241L;
	private JPanel contentPane;
	private JTextField txtNome;
	private JTextField txtPeso;
	
	private EntityManagerFactory emf = Persistence.createEntityManagerFactory("voleiPU");
	private EntityManager em = emf.createEntityManager();
	private Jogador jogador;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					JogadorFormAlterar frame = new JogadorFormAlterar();
					frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the frame.
	 */
	public JogadorFormAlterar() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 318, 437);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JLabel lblNome = new JLabel("Nome:");
		lblNome.setFont(new Font("Dialog", Font.BOLD, 14));
		lblNome.setBounds(10, 53, 53, 16);
		contentPane.add(lblNome);
		
		JLabel lblAltura = new JLabel("Altura (cm):");
		lblAltura.setFont(new Font("Dialog", Font.BOLD, 14));
		lblAltura.setBounds(10, 123, 87, 16);
		contentPane.add(lblAltura);
		
		JLabel lblPeso = new JLabel("Peso (kg):");
		lblPeso.setFont(new Font("Dialog", Font.BOLD, 14));
		lblPeso.setBounds(10, 150, 87, 16);
		contentPane.add(lblPeso);
		
		JLabel lblIdade = new JLabel("Idade:");
		lblIdade.setFont(new Font("Dialog", Font.BOLD, 14));
		lblIdade.setBounds(10, 177, 53, 16);
		contentPane.add(lblIdade);
		
		JLabel lblInserirJogadores = new JLabel("Alterar um jogador");
		lblInserirJogadores.setFont(new Font("Dialog", Font.BOLD, 14));
		lblInserirJogadores.setBounds(83, 11, 130, 29);
		contentPane.add(lblInserirJogadores);
		
		JLabel lblPosicao = new JLabel("Posição:");
		lblPosicao.setFont(new Font("Dialog", Font.BOLD, 14));
		lblPosicao.setBounds(10, 204, 66, 16);
		contentPane.add(lblPosicao);
		
		JLabel lblProfissional = new JLabel("Profissional (anos):");
		lblProfissional.setFont(new Font("Dialog", Font.BOLD, 14));
		lblProfissional.setBounds(10, 310, 142, 16);
		contentPane.add(lblProfissional);
		
		JLabel lblCamisa = new JLabel("Número da camisa:");
		lblCamisa.setFont(new Font("Dialog", Font.BOLD, 14));
		lblCamisa.setBounds(10, 337, 158, 16);
		contentPane.add(lblCamisa);
		
		txtNome = new JTextField();
		txtNome.setBounds(168, 52, 114, 20);
		contentPane.add(txtNome);
		txtNome.setColumns(10);
		
		JSpinner spnAltura = new JSpinner();
		spnAltura.setEnabled(false);
		spnAltura.setBounds(168, 122, 114, 20);
		contentPane.add(spnAltura);
		
		txtPeso = new JTextField();
		txtPeso.setEnabled(false);
		txtPeso.setBounds(168, 149, 114, 20);
		contentPane.add(txtPeso);
		txtPeso.setColumns(10);
		
		JSpinner spnIdade = new JSpinner();
		spnIdade.setEnabled(false);
		spnIdade.setBounds(168, 176, 114, 20);
		contentPane.add(spnIdade);
		
		DefaultListModel<PosicaoEnum> model = new DefaultListModel<>();
		JList<PosicaoEnum> lstPosicao = new JList<PosicaoEnum>(model);
		lstPosicao.setEnabled(false);
		lstPosicao.setSelectionMode(ListSelectionModel.SINGLE_SELECTION);
		lstPosicao.setBounds(168, 204, 114, 93);
		for(PosicaoEnum p: PosicaoEnum.values()) {
			model.addElement(p);
		}
		contentPane.add(lstPosicao);
		
		JSpinner spnProfissional = new JSpinner();
		spnProfissional.setEnabled(false);
		spnProfissional.setBounds(168, 309, 114, 20);
		contentPane.add(spnProfissional);
		
		JSpinner spnCamisa = new JSpinner();
		spnCamisa.setEnabled(false);
		spnCamisa.setBounds(168, 336, 114, 20);
		contentPane.add(spnCamisa);
		
		JButton btnAlterar = new JButton("Alterar");
		btnAlterar.setEnabled(false);
		btnAlterar.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				jogador = new Jogador();
				jogador.setNome(txtNome.getText());
				System.out.println(jogador.getNome());
				jogador.setAltura((Integer)spnAltura.getValue());
				jogador.setIdade((Integer)spnIdade.getValue());
				jogador.setNumeroCamisa((Integer)spnCamisa.getValue());
				jogador.setTempoProfissional((Integer)spnProfissional.getValue());
				jogador.setPeso((Float.parseFloat(txtPeso.getText())));
				jogador.setPosicao(PosicaoEnum.valueOf(model.getElementAt(lstPosicao.getSelectedIndex()).toString()));
				txtNome.setEnabled(true);
				spnAltura.setEnabled(false);
				spnIdade.setEnabled(false);
				spnCamisa.setEnabled(false);
				spnProfissional.setEnabled(false);
				txtPeso.setEnabled(false);
				lstPosicao.setEnabled(false);
				btnAlterar.setEnabled(false);
				em.getTransaction().begin();
				em.merge(jogador);
				em.getTransaction().commit();
				txtNome.setText("");
				spnAltura.setValue(0);
				spnIdade.setValue(0);
				spnCamisa.setValue(0);
				spnProfissional.setValue(0);
				txtPeso.setText("");
				lstPosicao.setSelectedValue(null, rootPaneCheckingEnabled);
			}
		});
		btnAlterar.setBounds(101, 364, 98, 26);
		contentPane.add(btnAlterar);
		
		JButton btnBuscar = new JButton("Buscar");
		btnBuscar.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				jogador = em.find(Jogador.class, txtNome.getText());
				if(jogador != null) {
					txtNome.setEnabled(false);
					spnAltura.setEnabled(true);
					spnAltura.setValue(jogador.getAltura());
					spnIdade.setEnabled(true);
					spnIdade.setValue(jogador.getIdade());
					spnCamisa.setEnabled(true);
					spnCamisa.setValue(jogador.getNumeroCamisa());
					spnProfissional.setEnabled(true);
					spnProfissional.setValue(jogador.getTempoProfissional());
					txtPeso.setEnabled(true);
					txtPeso.setText(jogador.getPeso() + "");
					lstPosicao.setEnabled(true);
					lstPosicao.setSelectedValue(jogador.getPosicao(), rootPaneCheckingEnabled);
					btnAlterar.setEnabled(true);
				}
				else {
					JOptionPane.showMessageDialog(null, "Jogador não existe");
				}
			}
		});
		btnBuscar.setBounds(101, 83, 98, 26);
		contentPane.add(btnBuscar);
	}
}
