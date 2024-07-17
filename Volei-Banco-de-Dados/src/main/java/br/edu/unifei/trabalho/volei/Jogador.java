package br.edu.unifei.trabalho.volei;

import javax.persistence.Entity;
import javax.persistence.EnumType;
import javax.persistence.Enumerated;
import javax.persistence.OneToOne;

import lombok.Data;
import lombok.EqualsAndHashCode;

@Data
@EqualsAndHashCode(callSuper = false)
@Entity
public class Jogador extends Pessoa {
	private static final long serialVersionUID = 9600418764951288L;
	@Enumerated(EnumType.STRING)
	private PosicaoEnum posicao;
	private int tempoProfissional;
	private int numeroCamisa;
	@OneToOne
	private Posicionamento posicionamento;
}
