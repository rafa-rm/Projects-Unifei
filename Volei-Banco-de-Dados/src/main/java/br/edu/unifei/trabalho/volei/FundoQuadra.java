package br.edu.unifei.trabalho.volei;

import javax.persistence.Entity;

import lombok.Data;
import lombok.EqualsAndHashCode;

@Data
@EqualsAndHashCode(callSuper = false)
@Entity
public class FundoQuadra extends Posicionamento {

	private static final long serialVersionUID = -1001490464213388786L;

	@Override
	public void realizaAcao() {
		System.out.println("Estou na defesa " + getPosicaoRotacao().name().toLowerCase());
	}
}
